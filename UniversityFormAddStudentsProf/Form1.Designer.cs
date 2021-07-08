
namespace WinFormsApp1
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.textBox4 = new System.Windows.Forms.TextBox();
            this.btnRead = new System.Windows.Forms.Button();
            this.btnSave = new System.Windows.Forms.Button();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.textBox3 = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.cbbStudentCourse = new System.Windows.Forms.ComboBox();
            this.label4 = new System.Windows.Forms.Label();
            this.cbbStudentSpecial = new System.Windows.Forms.ComboBox();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.txtStudentName = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.ScDegreeProfBox = new System.Windows.Forms.ComboBox();
            this.textBox5 = new System.Windows.Forms.TextBox();
            this.btnReadProf = new System.Windows.Forms.Button();
            this.btnSaveProf = new System.Windows.Forms.Button();
            this.filePathProf = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.fileNameProf = new System.Windows.Forms.TextBox();
            this.label8 = new System.Windows.Forms.Label();
            this.DepartProfBox = new System.Windows.Forms.ComboBox();
            this.label9 = new System.Windows.Forms.Label();
            this.AcadProfBox = new System.Windows.Forms.ComboBox();
            this.label10 = new System.Windows.Forms.Label();
            this.txtProfName = new System.Windows.Forms.TextBox();
            this.label11 = new System.Windows.Forms.Label();
            this.label12 = new System.Windows.Forms.Label();
            this.labelError = new System.Windows.Forms.Label();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.textBox4);
            this.groupBox1.Controls.Add(this.btnRead);
            this.groupBox1.Controls.Add(this.btnSave);
            this.groupBox1.Controls.Add(this.textBox2);
            this.groupBox1.Controls.Add(this.label5);
            this.groupBox1.Controls.Add(this.textBox3);
            this.groupBox1.Controls.Add(this.label6);
            this.groupBox1.Controls.Add(this.cbbStudentCourse);
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Controls.Add(this.cbbStudentSpecial);
            this.groupBox1.Controls.Add(this.textBox1);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.txtStudentName);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Location = new System.Drawing.Point(10, 9);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(304, 382);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Студент";
            // 
            // textBox4
            // 
            this.textBox4.Location = new System.Drawing.Point(23, 301);
            this.textBox4.Multiline = true;
            this.textBox4.Name = "textBox4";
            this.textBox4.Size = new System.Drawing.Size(246, 63);
            this.textBox4.TabIndex = 2;
            // 
            // btnRead
            // 
            this.btnRead.Location = new System.Drawing.Point(155, 263);
            this.btnRead.Name = "btnRead";
            this.btnRead.Size = new System.Drawing.Size(75, 23);
            this.btnRead.TabIndex = 12;
            this.btnRead.Text = "Четене";
            this.btnRead.UseVisualStyleBackColor = true;
            this.btnRead.Click += new System.EventHandler(this.btnRead_Click);
            // 
            // btnSave
            // 
            this.btnSave.Location = new System.Drawing.Point(50, 263);
            this.btnSave.Name = "btnSave";
            this.btnSave.Size = new System.Drawing.Size(75, 23);
            this.btnSave.TabIndex = 11;
            this.btnSave.Text = "Запис";
            this.btnSave.UseVisualStyleBackColor = true;
            this.btnSave.Click += new System.EventHandler(this.btnSave_Click);
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(113, 210);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(117, 23);
            this.textBox2.TabIndex = 10;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(23, 213);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(82, 15);
            this.label5.TabIndex = 9;
            this.label5.Text = "Път до файла";
            // 
            // textBox3
            // 
            this.textBox3.Location = new System.Drawing.Point(113, 181);
            this.textBox3.Name = "textBox3";
            this.textBox3.Size = new System.Drawing.Size(117, 23);
            this.textBox3.TabIndex = 8;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(23, 184);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(79, 15);
            this.label6.TabIndex = 7;
            this.label6.Text = "Име на файл";
            // 
            // cbbStudentCourse
            // 
            this.cbbStudentCourse.FormattingEnabled = true;
            this.cbbStudentCourse.Items.AddRange(new object[] {
            "1",
            "2",
            "3"});
            this.cbbStudentCourse.Location = new System.Drawing.Point(109, 126);
            this.cbbStudentCourse.Name = "cbbStudentCourse";
            this.cbbStudentCourse.Size = new System.Drawing.Size(121, 23);
            this.cbbStudentCourse.TabIndex = 6;
            this.cbbStudentCourse.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(23, 129);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(33, 15);
            this.label4.TabIndex = 5;
            this.label4.Text = "Курс";
            this.label4.Click += new System.EventHandler(this.label4_Click);
            // 
            // cbbStudentSpecial
            // 
            this.cbbStudentSpecial.FormattingEnabled = true;
            this.cbbStudentSpecial.Items.AddRange(new object[] {
            "KASP",
            "SP",
            "KSVT",
            "BK"});
            this.cbbStudentSpecial.Location = new System.Drawing.Point(109, 97);
            this.cbbStudentSpecial.Name = "cbbStudentSpecial";
            this.cbbStudentSpecial.Size = new System.Drawing.Size(121, 23);
            this.cbbStudentSpecial.TabIndex = 4;
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(113, 62);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(117, 23);
            this.textBox1.TabIndex = 3;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(23, 65);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(70, 15);
            this.label2.TabIndex = 2;
            this.label2.Text = "Фак. номер";
            // 
            // txtStudentName
            // 
            this.txtStudentName.Location = new System.Drawing.Point(113, 33);
            this.txtStudentName.Name = "txtStudentName";
            this.txtStudentName.Size = new System.Drawing.Size(117, 23);
            this.txtStudentName.TabIndex = 1;
            this.txtStudentName.TextChanged += new System.EventHandler(this.txtStudentName_TextChanged);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(23, 100);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(80, 15);
            this.label3.TabIndex = 0;
            this.label3.Text = "Специалност";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(23, 36);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(31, 15);
            this.label1.TabIndex = 0;
            this.label1.Text = "Име";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.ScDegreeProfBox);
            this.groupBox2.Controls.Add(this.textBox5);
            this.groupBox2.Controls.Add(this.btnReadProf);
            this.groupBox2.Controls.Add(this.btnSaveProf);
            this.groupBox2.Controls.Add(this.filePathProf);
            this.groupBox2.Controls.Add(this.label7);
            this.groupBox2.Controls.Add(this.fileNameProf);
            this.groupBox2.Controls.Add(this.label8);
            this.groupBox2.Controls.Add(this.DepartProfBox);
            this.groupBox2.Controls.Add(this.label9);
            this.groupBox2.Controls.Add(this.AcadProfBox);
            this.groupBox2.Controls.Add(this.label10);
            this.groupBox2.Controls.Add(this.txtProfName);
            this.groupBox2.Controls.Add(this.label11);
            this.groupBox2.Controls.Add(this.label12);
            this.groupBox2.Location = new System.Drawing.Point(324, 10);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(304, 381);
            this.groupBox2.TabIndex = 1;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Преподавател";
            // 
            // ScDegreeProfBox
            // 
            this.ScDegreeProfBox.FormattingEnabled = true;
            this.ScDegreeProfBox.Items.AddRange(new object[] {
            "доктор",
            "доктор на науките"});
            this.ScDegreeProfBox.Location = new System.Drawing.Point(134, 57);
            this.ScDegreeProfBox.Name = "ScDegreeProfBox";
            this.ScDegreeProfBox.Size = new System.Drawing.Size(121, 23);
            this.ScDegreeProfBox.TabIndex = 28;
            // 
            // textBox5
            // 
            this.textBox5.Location = new System.Drawing.Point(29, 293);
            this.textBox5.Multiline = true;
            this.textBox5.Name = "textBox5";
            this.textBox5.Size = new System.Drawing.Size(246, 63);
            this.textBox5.TabIndex = 16;
            // 
            // btnReadProf
            // 
            this.btnReadProf.Location = new System.Drawing.Point(161, 255);
            this.btnReadProf.Name = "btnReadProf";
            this.btnReadProf.Size = new System.Drawing.Size(75, 23);
            this.btnReadProf.TabIndex = 27;
            this.btnReadProf.Text = "Четене";
            this.btnReadProf.UseVisualStyleBackColor = true;
            this.btnReadProf.Click += new System.EventHandler(this.btnReadProf_Click);
            // 
            // btnSaveProf
            // 
            this.btnSaveProf.Location = new System.Drawing.Point(56, 255);
            this.btnSaveProf.Name = "btnSaveProf";
            this.btnSaveProf.Size = new System.Drawing.Size(75, 23);
            this.btnSaveProf.TabIndex = 26;
            this.btnSaveProf.Text = "Запис";
            this.btnSaveProf.UseVisualStyleBackColor = true;
            this.btnSaveProf.Click += new System.EventHandler(this.btnSaveProf_Click);
            // 
            // filePathProf
            // 
            this.filePathProf.Location = new System.Drawing.Point(138, 202);
            this.filePathProf.Name = "filePathProf";
            this.filePathProf.Size = new System.Drawing.Size(117, 23);
            this.filePathProf.TabIndex = 25;
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(29, 205);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(82, 15);
            this.label7.TabIndex = 24;
            this.label7.Text = "Път до файла";
            // 
            // fileNameProf
            // 
            this.fileNameProf.Location = new System.Drawing.Point(138, 173);
            this.fileNameProf.Name = "fileNameProf";
            this.fileNameProf.Size = new System.Drawing.Size(117, 23);
            this.fileNameProf.TabIndex = 23;
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(29, 176);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(79, 15);
            this.label8.TabIndex = 22;
            this.label8.Text = "Име на файл";
            // 
            // DepartProfBox
            // 
            this.DepartProfBox.FormattingEnabled = true;
            this.DepartProfBox.Items.AddRange(new object[] {
            "ИТ",
            "КТ",
            "МИТТП"});
            this.DepartProfBox.Location = new System.Drawing.Point(134, 120);
            this.DepartProfBox.Name = "DepartProfBox";
            this.DepartProfBox.Size = new System.Drawing.Size(121, 23);
            this.DepartProfBox.TabIndex = 21;
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(29, 121);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(50, 15);
            this.label9.TabIndex = 20;
            this.label9.Text = "Катедра";
            // 
            // AcadProfBox
            // 
            this.AcadProfBox.FormattingEnabled = true;
            this.AcadProfBox.Items.AddRange(new object[] {
            "асистент",
            "доцент",
            "професор"});
            this.AcadProfBox.Location = new System.Drawing.Point(134, 89);
            this.AcadProfBox.Name = "AcadProfBox";
            this.AcadProfBox.Size = new System.Drawing.Size(121, 23);
            this.AcadProfBox.TabIndex = 19;
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(29, 60);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(88, 15);
            this.label10.TabIndex = 17;
            this.label10.Text = "Научна степен";
            // 
            // txtProfName
            // 
            this.txtProfName.Location = new System.Drawing.Point(134, 25);
            this.txtProfName.Name = "txtProfName";
            this.txtProfName.Size = new System.Drawing.Size(121, 23);
            this.txtProfName.TabIndex = 15;
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Location = new System.Drawing.Point(29, 92);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(93, 15);
            this.label11.TabIndex = 13;
            this.label11.Text = "Акад. длъжност";
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.Location = new System.Drawing.Point(29, 28);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(31, 15);
            this.label12.TabIndex = 14;
            this.label12.Text = "Име";
            // 
            // labelError
            // 
            this.labelError.AutoSize = true;
            this.labelError.Location = new System.Drawing.Point(12, 411);
            this.labelError.Name = "labelError";
            this.labelError.Size = new System.Drawing.Size(44, 15);
            this.labelError.TabIndex = 2;
            this.labelError.Text = "label13";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(640, 537);
            this.Controls.Add(this.labelError);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.ComboBox cbbStudentCourse;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.ComboBox cbbStudentSpecial;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txtStudentName;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.TextBox textBox4;
        private System.Windows.Forms.Button btnRead;
        private System.Windows.Forms.Button btnSave;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox textBox3;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.ComboBox ScDegreeProfBox;
        private System.Windows.Forms.TextBox textBox5;
        private System.Windows.Forms.Button btnReadProf;
        private System.Windows.Forms.Button btnSaveProf;
        private System.Windows.Forms.TextBox filePathProf;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.TextBox fileNameProf;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.ComboBox DepartProfBox;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.ComboBox AcadProfBox;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.TextBox txtProfName;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.Label labelError;
    }
}

