package com.example1.demo.Controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example1.demo.dbo.OrderRequest;

@RestController
@RequestMapping("/api/flash-sale")
public class FlashSaleController {

	@Autowired
	private StringRedisTemplate redisTemplate;

	@PostMapping("/order")
	public ResponseEntity<String> placeOrder(@RequestBody OrderRequest request) {
		String stockKey = "product_stock:" + request.getProductId();
		String userKey = "user_purchased:" + request.getProductId() + ":" + request.getUserId();

		// 1. Kiểm tra giới hạn mua/người (Tối đa 2)
		String purchasedCount = redisTemplate.opsForValue().get(userKey);
		int currentPurchased = purchasedCount != null ? Integer.parseInt(purchasedCount) : 0;
		if (currentPurchased + request.getQuantity() > 2) {
			return ResponseEntity.badRequest().body("Vượt quá giới hạn mua (tối đa 2 sản phẩm)");
		}

		// 2. Kiểm tra tồn kho và trừ kho (Atomic sử dụng Lua Script hoặc decrement)
		Long remaining = redisTemplate.opsForValue().decrement(stockKey, request.getQuantity());

		if (remaining != null && remaining < 0) {
			redisTemplate.opsForValue().increment(stockKey, request.getQuantity()); // Hoàn kho nếu âm
			return ResponseEntity.badRequest().body("Sản phẩm đã hết hàng");
		}

		// 3. Cập nhật số lượng user đã mua và đẩy vào Queue xử lý DB sau
		redisTemplate.opsForValue().increment(userKey, request.getQuantity());
		// saveToQueue(request);

		return ResponseEntity.ok("Đặt hàng thành công! Đang xử lý...");
	}
}