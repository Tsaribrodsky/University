using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }



        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private bool filenameValid()
        {
            string name = textBox3.Text.Trim();
            string regex = @"^[0-9a-zA-Z_\-. ]+$";
            bool valid = Regex.IsMatch(name, regex);
            return valid;
        }

        private bool pathValid()
        {
            string name = textBox2.Text.Trim();
            string regex = @"[a-zA-Z]:[\\\/](?:[a-zA-Z0-9]+[\\\/])*([a-zA-Z0-9])";
            bool valid = Regex.IsMatch(name, regex);
            return valid;
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            labelError.Visible = true;

            if (!filenameValid())
            {
                labelError.Text = "Името на файла не е въведен правилно!";
                return;
            }
            else labelError.Text = "";

            if (!pathValid())
            {
                labelError.Text = "Пътят не е въведен правилно!";
                return;
            }
            else labelError.Text = "";

            Student st = new Student();
            if (!readStudentData(st))
                return;

            University uni1 = new University(st);
            if (textBox3.Text.Trim().Length == 0)
            {
                MessageBox.Show("Не е въведено име на файл!");
                return;
            }
            else uni1.FileName = textBox3.Text.Trim();

            if (textBox2.Text.Trim().Length == 0)
            {
                if (MessageBox.Show("Не е въведен път до файл! Файлът ще се търси в текущата директория. \nДа се продължи ли със записа?",
                    "Внимание!", MessageBoxButtons.YesNo) == DialogResult.No) return;
            }
            else uni1.PathName = textBox2.Text.Trim();

            try
            {
                uni1.FileWrite();
            }
            catch(IOException ex)
            {
                MessageBox.Show("Грешка при запис!");
            }
        }

        private bool readStudentData(Student st)
        {
            if (txtStudentName.Text.Trim().Length == 0)
            {
                MessageBox.Show("Не е въведено име на студент!");
                return false;
            }
            else st.Name = txtStudentName.Text.Trim();

            if (textBox1.Text.Trim().Length == 0)
            {
                MessageBox.Show("Не е въведен факултетен номер!");
                return false;
            }
            else st.FacNum = textBox1.Text.Trim();

            if (cbbStudentSpecial.Text.Trim().Length == 0)
            {
                MessageBox.Show("Не е избрана специалност!");
                return false;
            }
            else st.Specialty = cbbStudentSpecial.Text.Trim();

            if (cbbStudentCourse.Text.Trim().Length == 0)
            {
                MessageBox.Show("Не е избран курс!");
                return false;
            }
            else st.Course = cbbStudentCourse.Text.Trim();

            return true;
        }

        private void btnRead_Click(object sender, EventArgs e)
        {
            Student st = new Student();

            University uni1 = new University(st);
            if (textBox3.Text.Trim().Length == 0)
            {
                MessageBox.Show("Не е въведено име на файл!");
                return;
            }
            else uni1.FileName = textBox3.Text.Trim();

            if (textBox2.Text.Trim().Length == 0)
            {
                if (MessageBox.Show("Не е въведен път до файл! Файлът ще се търси в текущата директория. \nДа се продължи ли със записа?",
                    "Внимание!", MessageBoxButtons.YesNo) == DialogResult.No) return;
            }
            else uni1.PathName = textBox2.Text.Trim();

            try
            {
                uni1.FileRead();
                textBox4.Text = uni1.GetFullRecord();
            }
            catch (IOException ex)
            {
                MessageBox.Show("Грешка при четене!");
            }
        }

        private void btnSaveProf_Click(object sender, EventArgs e)
        {
            Prof pr = new Prof();
            if (!readProfData(pr))
                return;

            University uni1 = new University(pr);
            if (fileNameProf.Text.Trim().Length == 0)
            {
                MessageBox.Show("Не е въведено име на файл!");
                return;
            }
            else uni1.FileName = fileNameProf.Text.Trim();

            if (filePathProf.Text.Trim().Length == 0)
            {
                if (MessageBox.Show("Не е въведен път до файл! Файлът ще се търси в текущата директория. \nДа се продължи ли със записа?",
                    "Внимание!", MessageBoxButtons.YesNo) == DialogResult.No) return;
            }
            else uni1.PathName = filePathProf.Text.Trim();

            try
            {
                uni1.FileWrite();
            }
            catch (IOException ex)
            {
                MessageBox.Show("Грешка при запис!");
            }
        }

        private bool readProfData(Prof pr)
        {
            if (txtProfName.Text.Trim().Length == 0)
            {
                MessageBox.Show("Не е въведено име на преподавателя!");
                return false;
            }
            else pr.Name = txtProfName.Text.Trim();

            if (ScDegreeProfBox.Text.Trim().Length == 0)
            {
                MessageBox.Show("Не е избрана научна степен!");
                return false;
            }
            else pr.ScienceDegree = ScDegreeProfBox.Text.Trim();

            if (AcadProfBox.Text.Trim().Length == 0)
            {
                MessageBox.Show("Не е избрана академична длъжност!");
                return false;
            }
            else pr.AcademicPosition = AcadProfBox.Text.Trim();

            if (DepartProfBox.Text.Trim().Length == 0)
            {
                MessageBox.Show("Не е избрана катедра!");
                return false;
            }
            else pr.Department = DepartProfBox.Text.Trim();

            return true;
        }

        private void btnReadProf_Click(object sender, EventArgs e)
        {
            Prof pr = new Prof();

            University uni1 = new University(pr);
            if (fileNameProf.Text.Trim().Length == 0)
            {
                MessageBox.Show("Не е въведено име на файл!");
                return;
            }
            else uni1.FileName = fileNameProf.Text.Trim();

            if (filePathProf.Text.Trim().Length == 0)
            {
                if (MessageBox.Show("Не е въведен път до файл! Файлът ще се търси в текущата директория. \nДа се продължи ли със записа?",
                    "Внимание!", MessageBoxButtons.YesNo) == DialogResult.No) return;
            }
            else uni1.PathName = filePathProf.Text.Trim();

            try
            {
                uni1.FileRead();
                textBox5.Text = uni1.GetFullRecord();
            }
            catch (IOException ex)
            {
                MessageBox.Show("Грешка при четене!");
            }
        }

        private void txtStudentName_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
