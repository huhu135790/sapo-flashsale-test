
using Web5.Models;
using Web5.Repository;

namespace Web5.View.Repository
{
    public class LoaiSpQuocGia : IQuocGiacs
    {
        private readonly QlbanVaLiContext _context;

        public LoaiSpQuocGia(QlbanVaLiContext context)
        {
            _context = context;
        }

        public TQuocGium Add(TQuocGium quocGia)
        {
            throw new NotImplementedException();
        }

        public TQuocGium Delet(string maQuocGia)
        {
            throw new NotImplementedException();
        }

        public TQuocGium Delete(string maNuoc)
        {
            throw new NotImplementedException();
        }

        public IEnumerable<TQuocGium> GetAllQuocGia()
        {
            return _context.TQuocGia;
        }

        public TQuocGium GetQuocGia(string maQuocGia)
        {
            return _context.TQuocGia.Find(maQuocGia);
        }

        public TQuocGium Update(TQuocGium quocGia)
        {
            throw new NotImplementedException();
        }
    }
}
