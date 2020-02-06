
import os


def main():
        os.system("mkdir mining")
        os.chdir("mining")
        os.system("sudo apt-get install build-essential autoconf automake libtool pkg-config libudev-dev libcurl4-openssl-dev git ")
        os.system("git clone https://github.com/dmaxl/cgminer.git")
        os.system("cd cgminer && ./autogen.sh && ./configure --enable-scrypt --enable-gridseed")
        os.chdir("cgminer")
        os.system("make")


if __name__=="__main__":
        main()
