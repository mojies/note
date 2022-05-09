etc
---

    rk3588_firefly_itx_3588j:/system/etc # ls -l
    total 2247
    -rw-r--r-- 1 root root 398868 2022-05-05 07:08 NOTICE.xml.gz
    -rw-r--r-- 1 root root    561 2022-04-14 13:02 alarm_filter.xml
    -rw-r--r-- 1 root root 704324 2022-04-14 13:02 apns-conf.xml
    -rw-r--r-- 1 root root   5668 2022-04-14 13:02 audio_effects.conf
    drwxr-xr-x 2 root root   4096 2022-04-14 13:02 bluetooth
    -rw-r--r-- 1 root root   9368 2022-05-05 07:06 boot-image.bprof
    -rw-r--r-- 1 root root 224568 2022-05-05 07:06 boot-image.prof
    drwxr-xr-x 2 root root   4096 2022-04-14 13:02 bpf
    -rw-r--r-- 1 root root    877 2022-04-14 13:02 cgroups.json
    drwxr-xr-x 2 root root   4096 2022-04-14 13:02 classpaths
    drwxr-xr-x 2 root root   4096 2022-05-05 07:06 compatconfig
    -rw-r--r-- 1 root root  15055 2022-04-14 13:02 dirty-image-objects
    -rw-r--r-- 1 root root  32518 2022-04-14 13:02 event-log-tags
    -rw-r--r-- 1 root root  67158 2022-04-14 13:02 fonts.xml
    -r--r--r-- 1 root root      0 2022-04-14 13:02 fs_config_dirs
    -r--r--r-- 1 root root      0 2022-04-14 13:02 fs_config_files
    -rw-r--r-- 1 root root   1585 2022-04-14 13:02 gps_debug.conf
    -rw-r--r-- 1 root root      0 2022-04-14 13:02 group
    -rw-r--r-- 1 root root     56 2022-04-14 13:02 hosts
    drwxr-xr-x 3 root root   4096 2022-05-05 06:39 init
    -rw-r--r-- 1 root root   3882 2022-04-14 13:02 libnfc-nci.conf
    -rw-r--r-- 1 root root   1015 2022-05-05 07:08 linker.config.pb
    -rw-r--r-- 1 root root   2727 2022-04-14 13:02 media_profiles_V1_0.dtd
    -rw-r--r-- 1 root root   1157 2022-04-14 13:02 mke2fs.conf
    -rw-r--r-- 1 root root    389 2022-04-14 13:02 mkshrc
    -rw-r--r-- 1 root root    112 2022-04-14 13:02 operator_table
    -rw-r--r-- 1 root root      0 2022-04-14 13:02 passwd
    drwxr-xr-x 1 root root   3488 2022-05-05 11:34 permissions
    drwxr-xr-x 2 root root   4096 2022-04-14 13:02 ppp
    -rw-r--r-- 1 root root 605629 2022-04-14 13:02 preloaded-classes
    -rw-r--r-- 1 root root  18623 2022-04-28 11:42 protolog.conf.json.gz
    -rw-r--r-- 1 root root     40 2022-04-14 13:02 public.libraries-rockchip.txt
    -rw-r--r-- 1 root root    500 2022-04-14 13:02 public.libraries.txt
    -rw-r--r-- 1 root root   1282 2022-04-14 13:02 ql-ril.conf
    drwxr-xr-x 3 root root   4096 2022-04-14 13:02 res
    -rw-r--r-- 1 root root   1065 2022-04-14 13:02 rt_audio_config.xml
    -rw-r--r-- 1 root root   7955 2022-04-14 13:02 rt_video_config.xml
    -rw-r--r-- 1 root root    300 2022-04-14 13:02 sanitizer.libraries.txt
    drwxr-xr-x 2 root root   4096 2022-04-14 13:02 seccomp_policy
    drwxr-xr-x 4 root root   4096 2022-04-14 13:02 security
    drwxr-xr-x 3 root root   4096 2022-04-24 09:02 selinux
    -rw-r--r-- 1 root root  46832 2022-04-14 13:02 spn-conf.xml
    drwxr-xr-x 2 root root   4096 2022-04-14 13:02 sysconfig
    drwxr-xr-x 2 root root   4096 2022-04-14 13:02 task_profiles
    -rw-r--r-- 1 root root  12275 2022-04-14 13:02 task_profiles.json
    -rw-r--r-- 1 root root   3133 2022-04-14 13:02 ueventd.rc
    -rw-r--r-- 1 root root    433 2022-04-14 13:02 updatable-bcp-packages.txt
    drwxr-xr-x 3 root root   4096 2022-04-26 09:16 vintf
    -rw-r--r-- 1 root root   2598 2022-04-26 07:35 vndkcorevariant.libraries.txt
    -rw-r--r-- 1 root root    275 2022-04-14 13:02 wake_lock_filter.xml
    -rw-r--r-- 1 root root      0 2022-04-14 13:02 xtables.lock

etc/init
---

    rk3588_firefly_itx_3588j:/system/etc # ls -l init/
    total 288
    -rw-r--r-- 1 root root   117 2022-05-05 06:39 android.hidl.allocator@1.0-service.rc
    -rw-r--r-- 1 root root   166 2022-05-05 06:39 android.system.suspend@1.0-service.rc
    -rw-r--r-- 1 root root   500 2022-05-05 06:39 apexd.rc
    -rw-r--r-- 1 root root 22100 2022-05-05 06:39 atrace.rc
    -rw-r--r-- 1 root root   944 2022-05-05 06:39 atrace_userdebug.rc
    -rw-r--r-- 1 root root  2222 2022-05-05 06:39 audioserver.rc
    -rw-r--r-- 1 root root   113 2022-05-05 06:39 blank_screen.rc
    -rw-r--r-- 1 root root   185 2022-05-05 06:39 bootanim.rc
    -rw-r--r-- 1 root root   322 2022-05-05 06:39 bootstat-debug.rc
    -rw-r--r-- 1 root root  4670 2022-05-05 06:39 bootstat.rc
    -rw-r--r-- 1 root root  2919 2022-05-05 06:39 bpfloader.rc
    -rw-r--r-- 1 root root   223 2022-05-05 06:39 cameraserver.rc
    -rw-r--r-- 1 root root   111 2022-05-05 06:39 clean_scratch_files.rc
    -rw-r--r-- 1 root root   115 2022-05-05 06:39 credstore.rc
    -rw-r--r-- 1 root root   260 2022-05-05 06:39 drmserver.rc
    -rw-r--r-- 1 root root   719 2022-05-05 06:39 dumpstate.rc
    -rw-r--r-- 1 root root   485 2022-05-05 06:39 flags_health_check.rc
    -rw-r--r-- 1 root root   152 2022-05-05 06:39 gatekeeperd.rc
    -rw-r--r-- 1 root root    90 2022-05-05 06:39 gpuservice.rc
    -rw-r--r-- 1 root root   800 2022-05-05 06:39 gsid.rc
    -rw-r--r-- 1 root root  2129 2022-05-05 06:39 heapprofd.rc
    drwxr-xr-x 2 root root  4096 2022-05-05 06:39 hw
    -rw-r--r-- 1 root root   371 2022-05-05 06:39 hwservicemanager.rc
    -rw-r--r-- 1 root root    84 2022-05-05 06:39 idmap2d.rc
    -rw-r--r-- 1 root root   851 2022-05-05 06:39 incidentd.rc
    -rw-r--r-- 1 root root   659 2022-05-05 06:39 init-debug.rc
    -rw-r--r-- 1 root root  4674 2022-05-05 06:39 installd.rc
    -rw-r--r-- 1 root root  1479 2022-05-05 06:39 iorapd.rc
    -rw-r--r-- 1 root root   509 2022-05-05 06:39 keystore2.rc
    -rw-r--r-- 1 root root   557 2022-05-05 06:39 llkd-debuggable.rc
    -rw-r--r-- 1 root root  1229 2022-05-05 06:39 llkd.rc
    -rw-r--r-- 1 root root  2044 2022-05-05 06:39 lmkd.rc
    -rw-r--r-- 1 root root  2500 2022-05-05 06:39 logcatd.rc
    -rw-r--r-- 1 root root   888 2022-05-05 06:39 logd.rc
    -rw-r--r-- 1 root root   291 2022-04-14 13:02 logtagd.rc
    -rw-r--r-- 1 root root  1346 2022-05-05 06:39 lpdumpd.rc
    -rw-r--r-- 1 root root   142 2022-05-05 06:39 mdnsd.rc
    -rw-r--r-- 1 root root   166 2022-05-05 06:39 mediaextractor.rc
    -rw-r--r-- 1 root root   162 2022-05-05 06:39 mediametrics.rc
    -rw-r--r-- 1 root root   292 2022-05-05 06:39 mediaserver.rc
    -rw-r--r-- 1 root root   144 2022-04-26 03:23 mediatuner.rc
    -rw-r--r-- 1 root root   178 2022-05-05 06:39 mtpd.rc
    -rw-r--r-- 1 root root   590 2022-05-05 06:39 netd.rc
    -rw-r--r-- 1 root root   324 2022-05-05 06:39 odsign.rc
    -rw-r--r-- 1 root root  3278 2022-05-05 06:39 perfetto.rc
    -rw-r--r-- 1 root root   635 2022-05-05 06:39 profcollectd.rc
    -rw-r--r-- 1 root root   230 2022-05-05 06:39 racoon.rc
    -rw-r--r-- 1 root root   127 2022-05-05 06:39 recovery-persist.rc
    -rw-r--r-- 1 root root   912 2022-05-05 06:39 rss_hwm_reset.rc
    -rw-r--r-- 1 root root   400 2022-05-05 06:39 servicemanager.rc
    -rw-r--r-- 1 root root   178 2022-05-05 06:39 snapuserd.rc
    -rw-r--r-- 1 root root   225 2022-05-05 06:39 storaged.rc
    -rw-r--r-- 1 root root   360 2022-04-14 13:02 superuser.rc
    -rw-r--r-- 1 root root   578 2022-05-05 06:39 surfaceflinger.rc
    -rw-r--r-- 1 root root   309 2022-05-05 06:39 tombstoned.rc
    -rw-r--r-- 1 root root  2109 2022-05-05 06:39 traced_perf.rc
    -rw-r--r-- 1 root root   390 2022-05-05 06:39 uncrypt.rc
    -rw-r--r-- 1 root root   103 2022-05-05 06:39 usbd.rc
    -rw-r--r-- 1 root root   525 2022-05-05 06:39 vdc.rc
    -rw-r--r-- 1 root root   694 2022-05-05 06:39 vendor-464xlat.rc
    -rw-r--r-- 1 root root   326 2022-05-05 06:39 vold.rc
    -rw-r--r-- 1 root root   127 2022-05-05 06:39 wait_for_keymaster.rc
    -rw-r--r-- 1 root root  5715 2022-04-14 13:02 wifi.rc
    -rw-r--r-- 1 root root   135 2022-05-05 06:39 wificond.rc

public.libraries
---

    rk3588_firefly_itx_3588j:/system/etc # cat public.libraries.txt
    # See https://android.googlesource.com/platform/ndk/+/master/docs/PlatformApis.md
    libandroid.so
    libaaudio.so
    libamidi.so
    libbinder_ndk.so
    libc.so
    libcamera2ndk.so
    libdl.so
    libEGL.so
    libGLESv1_CM.so
    libGLESv2.so
    libGLESv3.so
    libicu.so
    libicui18n.so
    libicuuc.so
    libjnigraphics.so
    liblog.so
    libmediandk.so
    libm.so
    libnativehelper.so
    libnativewindow.so
    libneuralnetworks.so nopreload
    libOpenMAXAL.so
    libOpenSLES.so
    libRS.so
    libstdc++.so
    libsync.so
    libvulkan.so
    libwebviewchromium_plat_support.so
    libz.so
    rk3588_firefly_itx_3588j:/system/etc # cat public.libraries-rockchip.txt
    librknnhal_bridge.rockchip.so nopreload