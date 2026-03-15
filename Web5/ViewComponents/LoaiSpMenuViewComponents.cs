using Microsoft.AspNetCore.Mvc;
using System.Linq;
using Web5.Models;
using Web5.View.Repository;

namespace Web5.ViewComponents
{
    public class LoaiSpMenuViewComponent : ViewComponent
    {
        private readonly QlbanVaLiContext _context;

        public LoaiSpMenuViewComponent(QlbanVaLiContext context)
        {
            _context = context;
        }

        public IViewComponentResult Invoke()
        {
            var quocGiaList = _context.TQuocGia.ToList();
            return View(quocGiaList);
            // Gọi tới Views/Shared/Components/QuocGiaMenu/Default.cshtml
        }
    }
}
