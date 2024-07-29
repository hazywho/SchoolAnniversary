using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SS_Turret
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            port.Open();
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            writeToPort(new Point(e.X, e.Y));
        }

        public void writeToPort(Point coordinates)
        {
            port.Write(String.Format("X{0}Y{1}",
                (coordinates.X / (Size.Width / 180)),
                (coordinates.Y / (Size.Height / 180))));
        }
    }
}