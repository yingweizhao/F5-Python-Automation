with open('./gtm.conf','w') as gtm:
 for j in range(101,201):
    for i in range(101,201):
      cmd="""gtm server /Common/gen_100_"""+str(j)+"""_"""+str(i)+"""_1 {
    datacenter /Common/DC-A
    devices {
        device_100_"""+str(j)+"""_"""+str(i)+"""_1 {
            addresses {
               100."""+str(j)+"""."""+str(i)+""".1 { }
            }
        }
    }
    monitor /Common/tcp_a
    product generic-host
    virtual-servers {
        vs_100_"""+str(j)+"""_"""+str(i)+"""_1_80 {
            destination 100."""+str(j)+"""."""+str(i)+""".1:80
        }
    }
}
gtm pool a /Common/pool_100_"""+str(j)+"""_"""+str(i)+"""_1 {
    alternate-mode none
    fallback-mode drop-packet
    members {
        /Common/gen_100_"""+str(j)+"""_"""+str(i)+"""_1:vs_100_"""+str(j)+"""_"""+str(i)+"""_1_80 {
            member-order 0
        }
    }
}
gtm wideip a /Common/ym."""+str(j)+"""."""+str(i)+""".com {
    pools {
        /Common/pool_100_"""+str(j)+"""_"""+str(i)+"""_1 {
            order 0
        }
    }
} 
"""


      print cmd
      gtm.write(cmd)
gtm.close()
