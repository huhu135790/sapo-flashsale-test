using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Web5.Models.ProductModel;
using Web5.Models;
using Web5.Models.ProductModel;

namespace Web4.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ProductAPIController : Controller
    {


        QlbanVaLiContext db = new QlbanVaLiContext();
        [HttpGet]
        public IEnumerable<product> GetAllProducts()
        {
            var sanPham = (from p in db.TDanhMucSps
                           select new product
                           {
                               MaSp = p.MaSp,
                               TenSp = p.TenSp,
                               MaLoai = p.MaLoai,
                               AnhDaiDien = p.AnhDaiDien,
                               GiaLonNhat = p.GiaLonNhat,
                               GiaNhoNhat = p.GiaNhoNhat


                           }).ToList();
            return sanPham;
        }
        [HttpGet("quocgia/{maNuoc}")]
        public IEnumerable<product> GetProductsByCountry(string maNuoc)
        {
            var sanPham = db.TDanhMucSps
                .Where(p => p.MaNuocSx == maNuoc)
                .Select(p => new product
                {
                    MaSp = p.MaSp,
                    TenSp = p.TenSp,
                    MaLoai = p.MaLoai,
                    AnhDaiDien = p.AnhDaiDien,
                    GiaLonNhat = p.GiaLonNhat,
                    GiaNhoNhat = p.GiaNhoNhat,
                    TenNuoc = p.MaNuocSxNavigation.TenNuoc
                })
                .ToList();

            return sanPham;
        }


    }
}
