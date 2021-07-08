using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WinFormsApp1
{
    class Prof : FileWork
    {
        public string Name { set; get; }
        public string ScienceDegree { set; get; }
        public string AcademicPosition { set; get; }
        public string Department { set; get; }

        public void fileWrite(StreamWriter sw)
        {
            sw.WriteLine(Name);
            sw.WriteLine(ScienceDegree);
            sw.WriteLine(AcademicPosition);
            sw.WriteLine(Department);
        }

        public void fileRead(StreamReader sr)
        {
            Name = sr.ReadLine();
            ScienceDegree = sr.ReadLine();
            AcademicPosition = sr.ReadLine();
            Department = sr.ReadLine();
        }

        public string getString()
        {
            return $"Име: {this.Name} Научна степен: {this.ScienceDegree} Академична длъжност: {this.AcademicPosition} Катедра: {this.Department}";
        }
    }
}
