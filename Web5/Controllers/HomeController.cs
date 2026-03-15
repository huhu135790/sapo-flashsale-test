using Azure;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Storage;
using System.Diagnostics;
using Web5.Models;
using Web5.ViewModel;
using Web5.Repository;

using X.PagedList;
using X.PagedList.Extensions;

namespace Web5.Controllers
{
    public class HomeController : Controller
    {
        QlbanVaLiContext db = new QlbanVaLiContext();
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index(string maNuoc, int? page)
        {
            var listSanPham = db.TDanhMucSps.AsQueryable();

            if (!string.IsNullOrEmpty(maNuoc))
            {
                listSanPham = listSanPham.Where(x => x.MaNuocSx == maNuoc);
            }

            int pageNumber = page ?? 1;
            int pageSize = 12;

            var lst = listSanPham.OrderBy(x => x.TenSp).ToPagedList(pageNumber, pageSize);
           
            ViewBag.DanhSachQuocGia = db.TQuocGia.ToList();

            return View(lst);
        }

        public IActionResult DoanhNhan(int? page)
        {
            int pageNumber = page ?? 1;
            int pageSize = 12;

            var doanhNhanProducts = db.TDanhMucSps
                .Where(x => x.MaDt == "maDt") // hoặc giá trị nhận diện “Doanh Nhân”
                .OrderBy(x => x.TenSp)
                .ToPagedList(pageNumber, pageSize);

            ViewBag.DanhSachQuocGia = db.TQuocGia.ToList();

            return View(doanhNhanProducts); // View riêng cho doanh nhân
        }


        public IActionResult SanPhamTheoQuocGia(string maQuocGia, int? page)
        {
            var listSanPham = db.TDanhMucSps
                                .Where(x => x.MaNuocSx  == maQuocGia)
                                .OrderBy(x => x.TenSp)
                                .AsNoTracking();

            int pageNumber = page == null || page < 1 ? 1 : page.Value;
            int pageSize = 12;

            PagedList<TDanhMucSp> lst = new PagedList<TDanhMucSp>(listSanPham, pageNumber, pageSize);

            ViewBag.maQuocGia = maQuocGia;

            return View(lst);
        }
        public IActionResult ProductDeta(string maSP)
        {
            var sanPham = db.TDanhMucSps.SingleOrDefault(x => x.MaSp == maSP);
            var anhSanPham = db.TAnhSps.Where(x => x.MaSp == maSP).ToList();
            var homeProductDeataVieWModel = new HomeproductDeataViewModel
            {
                danhMucSp = sanPham,
                anhSP = anhSanPham

            };
            return View(homeProductDeataVieWModel);
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
