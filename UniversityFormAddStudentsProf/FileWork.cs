using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WinFormsApp1
{
    public interface FileWork
    {
        void fileWrite(StreamWriter sw);
        void fileRead(StreamReader sr);
        string getString();
    }
}
