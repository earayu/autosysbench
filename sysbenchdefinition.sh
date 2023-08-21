sysbench_vtgate_4_8_16_25_50_75_100_125_150_175=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-vtgate-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.251.240,user:root,port:15306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:4 8 16 25 50 75 100 125 150 175,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_mysql_4_8_16_25_50_75_100_125_150_175=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-mysql-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.134.200,user:root,password:sf2gxx9r,port:3306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:4 8 16 25 50 75 100 125 150 175,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_vtgate_150=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-vtgate-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.251.240,user:root,port:15306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:150,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_vtgate_125=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-vtgate-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.251.240,user:root,port:15306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:125,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_vtgate_100=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-vtgate-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.251.240,user:root,port:15306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:100,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_vtgate_75=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-vtgate-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.251.240,user:root,port:15306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:75,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_vtgate_50=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-vtgate-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.251.240,user:root,port:15306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:50,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_vtgate_25=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-vtgate-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.251.240,user:root,port:15306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:25,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_vtgate_16=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-vtgate-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.251.240,user:root,port:15306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:16,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_vtgate_8=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-vtgate-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.251.240,user:root,port:15306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:8,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_vtgate_4=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-vtgate-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.251.240,user:root,port:15306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:4,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_mysql_4=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-mysql-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.134.200,user:root,password:sf2gxx9r,port:3306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:4,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_mysql_8=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-mysql-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.134.200,user:root,password:sf2gxx9r,port:3306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:8,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_mysql_16=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-mysql-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.134.200,user:root,password:sf2gxx9r,port:3306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:16,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_mysql_25=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-mysql-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.134.200,user:root,password:sf2gxx9r,port:3306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:25,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_mysql_50=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-mysql-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.134.200,user:root,password:sf2gxx9r,port:3306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:50,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_mysql_75=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-mysql-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.134.200,user:root,password:sf2gxx9r,port:3306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:75,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_mysql_100=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-mysql-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.134.200,user:root,password:sf2gxx9r,port:3306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:100,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_mysql_125=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-mysql-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.134.200,user:root,password:sf2gxx9r,port:3306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:125,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_mysql_150=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-mysql-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.134.200,user:root,password:sf2gxx9r,port:3306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:150,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_vtgate_175=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-vtgate-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.251.240,user:root,port:15306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:175,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_mysql_175=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-mysql-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "mode:run,driver:mysql,host:172.16.134.200,user:root,password:sf2gxx9r,port:3306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:175,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)