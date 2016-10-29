# !/bin/bash

build_basic() {
        OBJ="Building basic funtion tests"

        SrcPath=${BENCH_PATH}"493.basic"
   myOBJPATH=${INSTALL_DIR}/basic/
   mkdir -p $myOBJPATH
        #pushd $SrcPath
                   cp  $SrcPath/*  $myOBJPATH
         #popd
        current_pwd=`pwd`
        echo $current_pwd
}

build_iperf() {
        SrcPath=${BENCH_PATH}"420.iperf"
        MYPWD=${PWD}
      BuildPATH="$MYPWD/build.iperf"
      TOP_SRCDIR="$MYPWD/$SrcPath"
   myOBJPATH=${INSTALL_DIR}/bin
    #exist_iperf=$(find $myOBJPATH -name 'iperf')
    #if [ "$exist_iperf"x -ne ""x ]; then
    #    return 0
    #fi
	mkdir -p $BuildPATH

        if [ $ARCH = "x86_64" -o $ARCH = "x86_32" ] 
        then
		pushd $BuildPATH
                $TOP_SRCDIR/configure
                make -s
                cp src/iperf $myOBJPATH
		popd
		rm -rf $BuildPATH
        fi

        if [ $ARCH = "arm_64" -o $ARCH = "arm_32" ]
        then
            echo ${GCC//gcc/g++}
		pushd $BuildPATH
                ac_cv_func_malloc_0_nonnull=yes $TOP_SRCDIR/configure --host=$ARMCROSS CC=$GCC CXX=${GCC//gcc/g++}
        	make 
	        cp src/iperf $myOBJPATH
		popd
		rm -rf $BuildPATH
        fi
}

build_busybox()
{
    set -e
        SrcPath=${BENCH_PATH}"491.busybox"
   myOBJPATH=${INSTALL_DIR}/bin
   mkdir -p $myOBJPATH
        if [ $ARCH = "x86_64" -o $ARCH = "x86_32" ]
            then
                    pushd $SrcPath
                    make defconfig       
                    make -s      
                    cp -r busybox $myOBJPATH
            make distclean     
                    popd
        fi

        if [ $ARCH = "arm_64" -o $ARCH = "arm_32" ]
        then
                pushd $SrcPath
                prefix_gcc=${GCC//gcc/ }
                #echo $prefix_gcc

      make ARCH=ARM CROSS_COMPILE=$prefix_gcc defconfig     
                make ARCH=ARM CROSS_COMPILE=$prefix_gcc -s       
                cp -r busybox  $myOBJPATH
                make distclean     
                popd
        fi
}

build_i2c_test() {
        OBJ="Building i2c test tools"

        SrcPath=${BENCH_PATH}"492.i2c_test"
   myOBJPATH=${INSTALL_DIR}/bin
   mkdir -p $myOBJPATH

        if [ "$ARCH" = "arm_64" -o  "$ARCH" = "arm_32" ]; then
            pushd $SrcPath
        $GCC -o i2c_op i2c_op.c
        cp  i2c_op $myOBJPATH

            make CC=$GCC -s
            cp tools/i2cdetect tools/i2cdump tools/i2cget tools/i2cset $myOBJPATH
            make clean
            rm -fr i2c_op
            popd
        fi
        if [ "$ARCH" = "x86" ]; then
            push $SrcPath
        gcc -o i2c_op i2c_op.c
        cp  i2c_op $myOBJPATH

            make  -s
            cp tools/i2cdetect tools/i2cdump tools/i2cget tools/i2cset $myOBJPATH
            make clean
        rm -fr i2c_op
            popd
        fi
}

build_memtester()
{
    set -e
    set -x

        SrcPath=${BENCH_PATH}"415.memtester"
   myOBJPATH=${INSTALL_DIR}/bin
   mkdir -p $myOBJPATH
        if [ $ARCH = "x86_64" -o $ARCH = "x86_32" ]
            then
                    pushd $SrcPath
                    make -s     
                    cp -r memtester $myOBJPATH
            make clean     
                    popd
        fi

        if [ $ARCH = "arm_64" -o $ARCH = "arm_32" ]
        then
                pushd $SrcPath
                
            if [ "$(cat conf-cc | grep 'gcc')"x != ""x ]
            then
                sed -i "s/gcc/$GCC/g" conf-cc
                sed -i "s/gcc/$GCC/g" conf-ld
            else
                sed -i "s/cc/$GCC/g" conf-cc
                sed -i "s/cc/$GCC/g" conf-ld
            fi
                make      
                cp -r memtester $myOBJPATH
                make clean     
                sed -i "s/$GCC/gcc/g" conf-cc
                sed -i "s/$GCC/gcc/g" conf-ld
                popd
        fi
}

#build_memtester
#build_iperf
#build_busybox
#build_i2c_test
build_basic

