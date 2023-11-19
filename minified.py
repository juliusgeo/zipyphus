import sys;itls,colls,binasc,struct,time=[\
 __import__(i) for i in("itertools",\
"collections","binascii","struct","time")];\
s=sys.stdin.read();(MOFFSET,MLENGTH,\
              FILE_NAME,ZIP_NAME,
             idx)=(2047,31,"a.txt"
            , "a.zip",  0); \
           compressed=[((*\
           lo,s[idx]),idx:=\
          idx+lo[1])[0] for\
         _ in itls.takewhile(
          lambda _:idx<len(
         s),iter(int, None))
        if(lo:=max([(i,l\
       ) if(l:=min(sum(\
      1 for _ in itls.\
     takewhile(lambda x\
     :x[0]==x[1],zip(\
    itls.cycle(s[: \
    idx][-i:]),s[idx\
   :],),)),MLENGTH,\
  ))>2 else(0,1)for i
   in range(1,(min(
 idx,MOFFSET)+1))\
if s[:idx][-i]==s[\
idx:][0]],default \
=(0,1),key= lambda x:x[1],))];it="110"+"".join(\
["{:0{}b}".format(*( lambda n:(int(bin(n+\
0b00110000),2),8 if n<144 else int(bin(n-144+\
 0b110010000),2),9 if n<257 else int(bin(n-257+\
\
\
\
0b0010100),2),7 if n<280\
else int(bin(n-280+\
  0b11000000),2),8 if n<\
   288 else(),))(ord\
   (tok[2]))) if\
    tok[1]<=1 else(\
   ("{:07b}".\
   format((leco:=\
   ( lambda n:((n,0\
   ,0) if n<=2 else(\
   254+n,0,0) if n\
   <=10 else(265+(\
   n-11)//2,(n-11\
   )%2,1) if n<=18\
    else(269+(n-19\
   )//4,(n-19)%4,\
   2) if n<=34 else(\
   273+(n-35)//8,\
   (n-35)%8,3) if n\
   <=66 else(277+(\
   n-67)//16,(n-\
   67)%16,4) if n<=\
   130 else(281+(n\
   -131)//32,(n-\
   131)%32,5) if n<\
   258 else(285,0,0)\
   if n==258 else()))\
(tok[1]))[0])[-7:])+(\
"{:0{}b}".format(*leco[1:])\
[-leco[2]:][::-1] if leco[2]\
\
\
\
>=1 else"")+("{:05b}".format((deco:=(\
lambda n:((n-1,0,0) if n<=4 else((n-5)//2+4,
(n-5),1) if n<=8 else((n-9)//4+6,(n-9),2\
    ) if n<=16 else(       (n-17)//8+8,(n-\
    17),3) if n<=32        else((n-33)//\
    16+10,(n-33),          4) if n<=64 else\
    ((n-65)//32+           12,(n-65),5)\
    if n<=128 else         ((n-129)//64+\
    14,(n-129),6)         if n<=256 else\
    ((n-257)//128         +16,(n-257),7)if
    n<=512 else((          n-513)//256+18\
    ,(n-513),8) if         n<=1024 else(
    (n-1025)//512+        20,(n-1025),9
    ) if n<=2048          else((n-2049)
    //1024+22,(n-         2049),10) if
    n<=4096 else((n-4097)//2048+
    24,(n-4097),11) if n<=\
    8192 else((n-8193)//\
    4096+26,(n-193),
    12)if n<=16384
    else((n-16385)//
    8192+28,(n-16385
    ),13)if n<=32768
    else()))(tok[0])
    )[0])[-5:])+ ( \
    "{:0{}b}".format(*deco[1:])[-deco[2]:][\
::-1] if deco[2]>=1 else"")) for tok in\
 compressed]);bb=(b"".join([int(it[\
\
\
\
i:i+8][::-1],2).              to_bytes(1,byteorder=\
"big",signed=False           )for i in range(0,len(it
 ),8)])+b"\x00");            (open(ZIP_NAME,"wb").
  write(((lh:=(              b"PK\003\004"+
   struct.pack(            "<2B4HL2L2H"
    ,20,20,0,             8,*(args:=(
    ((mtime:=time.       localtime(\
     )).tm_year-        1980)<<9|\
      mtime.tm_mon     <<5|mtime.
      tm_mday,mtime.  tm_hour<<\
        11|mtime.tm_min<<5|\
         mtime.tm_sec//2,\
         binasc.crc32(s:=\
         s.encode("ascii")
         ),len(bb),len(s\
         ),len(fnbytes:=\
         FILE_NAME.encode
         ("ascii")),)),0,
         )+fnbytes))+bb+(
         cdh:=( #######
         b"PK\001\002"+\
         struct.pack(\
         "<4B4HL2L5H2L",
         20,20,20,20,0,\
         8,*args,0,0,0,0
         ,0x20,0,)+fnbytes
    ))+struct.pack("<4s4H2LH",\
    b"PK\x05\x06",0,0,1,1,len(cdh),\
    len(lh)+args[3],0,))));#juliusgeo
