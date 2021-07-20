using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WinFormsApp1
{
    class Student : FileWork
    {
        public string Name { set; get; }
        public string FacNum { set; get; }
        public string Specialty { set; get; }
        public string Course { set; get; }

        public void fileWrite(StreamWriter sw)
        {
            sw.WriteLine(Name);
            sw.WriteLine(FacNum);
            sw.WriteLine(Specialty);
            sw.WriteLine(Course);
        }

        public void fileRead(StreamReader sr)
        {
            Name = sr.ReadLine();
            FacNum = sr.ReadLine();
            Specialty = sr.ReadLine();
            Course = sr.ReadLine();
        }

        public string getString()
        {
            return $"Име: {this.Name} Фак. номер: {this.FacNum} Специалност: {this.Specialty} Курс: {this.Course}";
        }
    }
}
