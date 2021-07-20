using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WinFormsApp1
{
    class University
    {
        FileWork person;
        string fileName;
        string pathName;

        public University(FileWork person)
        {
            this.person = person;
        }

        public University(FileWork person, string fileName, string pathName)
        {
            this.person = person;
            this.fileName = fileName;
            this.pathName = pathName;
        }

        public string FileName { get { return fileName; } set { fileName = value; } }
        public string PathName { get { return pathName; } set { pathName = value; } }

        public void FileWrite()
        {
            StreamWriter sw = new StreamWriter(pathName + fileName);
            person.fileWrite(sw);
            sw.Close();
        }

        public void FileRead()
        {
            StreamReader sw = new StreamReader(pathName + fileName);
            person.fileRead(sw);
            sw.Close();
        }

        public string GetFullRecord()
        {
            return person.getString();
        }
    }
}
