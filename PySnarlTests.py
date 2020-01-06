import PySnarl
import unittest, time, wx
from path import path

class TestSnarlFunctions(unittest.TestCase):
    
    def setUp(self):
        self.startSnarl()
        self.msg = PySnarl.SnarlMessage()
        self.app = wx.PySimpleApp()
        self.frame = wx.Frame(None, wx.ID_ANY, "Hello World")
        
    def tearDown(self):
        self.frame = None
        self.msg = None
        if self.pid > 0:
            self.stopSnarl()
        del self.app

    def test0001versionstarted(self):
        (a, b) = PySnarl.snGetVersion()
        self.assert_(type(a) == int or type(a) == long)
        self.assert_(type(b) == int or type(b) == long)

    def test0002versionstopped(self):
        self.stopSnarl()
        self.assert_(PySnarl.snGetVersion() == False)

    def test0003versionexstart(self):
        a = PySnarl.snGetVersionEx()
        self.assert_(type(a) == int or type(a) == long)

    def test0004versionexstopped(self):
        self.stopSnarl()
        self.assert_(PySnarl.snGetVersionEx() == False)

    def test0005snShowMessage(self):
        time.sleep(2)
        a = PySnarl.snShowMessage("test", "test")
        self.assert_( a == 633L )
        a = PySnarl.snShowMessage("test", "test")
        self.assert_( a == 634L )

    def test0006snShowMessageStopped(self):
        self.stopSnarl()
        a = PySnarl.snShowMessage("test", "test")
        self.assert_( a == False )
        
    def test0007snRegisterConfig(self):
        time.sleep(2)
        a = PySnarl.snRegisterConfig(self.frame.Handle, "unittest App", 0)
        self.assert_( a == 0L )

    def test0008snRegisterConfig2(self):
        time.sleep(2)
        p = path('.').abspath()
        a = PySnarl.snRegisterConfig2(self.frame.Handle, "unittest App", 0, p + "general.png")
        self.assert_( a == 0L )

    def test0009snRegisterAlert(self):
        time.sleep(2)
        p = path('.').abspath()
        PySnarl.snRegisterConfig(self.frame.Handle, "unittest App", 0)
        a = PySnarl.snRegisterAlert("unittest App", "testcase")
        self.assert_( a == 0L )
        b = PySnarl.snShowMessageEx('testcase', 'test', 'test')
        self.assert_( b == 634L )
        c = PySnarl.snShowMessageEx('testcase', 'test', 'test', hWndFrom=self.frame.Handle)
        self.assert_( c == 635L )
        d = PySnarl.snShowMessageEx('testcase', 'test', 'test', hWndFrom=0)
        self.assert_( d == PySnarl.M_BAD_HANDLE )
        e = PySnarl.snShowMessageEx('testcase', 'test', 'test', hWndFrom=1)
        self.assert_( e == PySnarl.M_NOT_FOUND )
        
    def test0010snRevokeConfig(self):
        time.sleep(2)
        PySnarl.snRegisterConfig(self.frame.Handle, "unittest App", 0)
        a = PySnarl.snRevokeConfig(self.frame.Handle)
        self.assert_(a == 0L)
        b = PySnarl.snRevokeConfig(self.frame.Handle)
        self.assert_(b == PySnarl.M_NOT_FOUND)
        c = PySnarl.snShowMessageEx('testcase', 'test', 'test')
        self.assert_( c == PySnarl.M_BAD_HANDLE )
        d = PySnarl.snShowMessageEx('testcase', 'test', 'test', hWndFrom=self.frame.Handle)
        self.assert_( d == PySnarl.M_NOT_FOUND )
        

    def startSnarl(self):
        import subprocess
        self.pid = subprocess.Popen(['d:/Snarl/snarl.exe']).pid
        time.sleep(1)
        
    def stopSnarl(self):
        import ctypes
        h = ctypes.windll.Kernel32.OpenProcess(1, 0, self.pid)
        ctypes.windll.Kernel32.TerminateProcess(h, -1)
        ctypes.windll.Kernel32.CloseHandle(h)
        self.pid = 0
        time.sleep(1)
 
if __name__ == '__main__':
    unittest.main()
