package com.example1.demo;

import org.junit.jupiter.api.Test;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

public class FlashSaleControllerTest {

	@Test
	void testOrder() {

		String url = "http://localhost:8081/api/flash-sale/order";

		RestTemplate restTemplate = new RestTemplate();

		String json = """
				{
				  "userId": 1,
				  "productId": 1,
				  "quantity": 1
				}
				""";

		HttpHeaders headers = new HttpHeaders();
		headers.setContentType(MediaType.APPLICATION_JSON);

		HttpEntity<String> request = new HttpEntity<>(json, headers);

		ResponseEntity<String> response = restTemplate.postForEntity(url, request, String.class);

		System.out.println(response.getBody());
	}
}