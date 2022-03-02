import optparse

par = optparse.OptionParser(
    usage = 'usage: %prog --bit 32 or --bit 64'
)

par.add_option(
    '--bit',help='Masukan bit hp mu contoh: --bit 64',default=None
)
(arg,opt) = par.parse_args()

if __name__ == "__main__":
   try:
       if(arg.bit=="64"):
       	__import__("app64").hencet_memek()
       elif(arg.bit=="32"):
       	__import__("app32").hencet_memek()
       else:
       	print(" * Jika hpmu 64 bit ketik: python run.py --bit 64, Jika hpmu 32 biy ketik: python run.py --bit 32\n")
   except Exception as e:
       exit(str(e))