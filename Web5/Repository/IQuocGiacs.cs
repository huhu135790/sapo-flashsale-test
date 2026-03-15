using Web5.Models;

namespace Web5.Repository
{
    public interface IQuocGiacs
    {
        TQuocGium Add(TQuocGium quocGia);
        TQuocGium Update(TQuocGium quocGia);
        TQuocGium Delete(string maNuoc);
        TQuocGium GetQuocGia(string maNuoc);
        IEnumerable<TQuocGium> GetAllQuocGia();
    }
}
