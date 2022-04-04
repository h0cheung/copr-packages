Name:           librime
Version:        1.7.3
Release:        5%{?dist}
Summary:        Rime Input Method Engine Library

License:        GPLv3
URL:            https://rime.im/
Source0:        https://github.com/rime/librime/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/rime/librime/issues/462
Patch0:         librime-boost176-exp.patch
Requires:       lua

BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  cmake, opencc-devel
BuildRequires:  boost-devel >= 1.46
BuildRequires:  zlib-devel
BuildRequires:  glog-devel, gtest-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  gflags-devel
BuildRequires:  marisa-devel
BuildRequires:  leveldb-devel
BuildRequires:  capnproto, capnproto-devel
BuildRequires:  lua-devel
BuildRequires:  bash

%description
Rime Input Method Engine Library

Support for shape-based and phonetic-based input methods,
including those for Chinese dialects.

A selected dictionary in Traditional Chinese,
powered by opencc for Simplified Chinese output.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
The %{name}-tools package contains tools for %{name}.


%prep
%autosetup -p1

%build
bash install-plugins.sh lotem/librime-octagram
bash install-plugins.sh hchunhui/librime-lua
bash install-plugins.sh rime/librime-charcode
%cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_MERGED_PLUGINS=Off -DENABLE_EXTERNAL_PLUGINS=On
%cmake_build


%install
%cmake_install


%ldconfig_scriptlets


%files
%doc README.md LICENSE
%{_libdir}/*.so.*
%{_libdir}/rime-plugins/*.so


%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/rime.pc
%dir %{_datadir}/cmake/rime
%{_datadir}/cmake/rime/RimeConfig.cmake


%files tools
%{_bindir}/rime_deployer
%{_bindir}/rime_dict_manager
%{_bindir}/rime_patch


%changelog
* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Neal Gompa <ngompa@fedoraproject.org> - 1.7.2-4
- Rebuild for capnproto 0.9.1

* Mon Aug 09 2021 Jonathan Wakely <jwakely@redhat.com> - 1.7.2-3
- Patched and rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Peng Wu <pwu@redhat.com> - 1.7.2-1
- Update to 1.7.2

* Mon May 10 2021 Jonathan Wakely <jwakely@redhat.com> - 1.6.1-5
- Rebuilt for removed libstdc++ symbols (#1937698)

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 1.6.1-4
- Rebuilt for removed libstdc++ symbol (#1937698)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.6.1-2
- Rebuilt for Boost 1.75

* Thu Dec 17 2020 Peng Wu <pwu@redhat.com> - 1.6.1-1
- Update to 1.6.1

* Wed Aug  5 2020 Peng Wu <pwu@redhat.com> - 1.5.3-6
- Use cmake macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 1.5.3-3
- Rebuilt for Boost 1.73

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 22 2019 Peng Wu <pwu@redhat.com> - 1.5.3-1
- Update to 1.5.3

* Fri Oct 18 2019 Richard Shaw <hobbes1069@gmail.com> - 1.3.2-5
- Rebuild for yaml-cpp 0.6.3.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.3.2-2
- Rebuilt for Boost 1.69

* Wed Nov 21 2018 Peng Wu <pwu@redhat.com> - 1.3.2-1
- Update to 1.3.2

* Wed Oct 10 2018 Sérgio Basto <sergio@serjux.com> - 1.2-24
- Rebuit for gflags-2.2.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 1.2-22
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Wed Feb 14 2018 Richard Shaw <hobbes1069@gmail.com> - 1.2-21
- Rebuild for yaml-cpp 0.6.0.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.2-19
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 1.2-16
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 1.2-15
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Jonathan Wakely <jwakely@redhat.com> - 1.2-12
- Rebuilt for Boost 1.63

* Tue Aug 23 2016 Richard Shaw <hobbes1069@gmail.com> - 1.2-11
- Rebuild for updated yaml-cpp

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 1.2-10
- Rebuilt for linker errors in boost (#1331983)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 1.2-8
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.2-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.2-5
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Kalev Lember <kalevlember@gmail.com> - 1.2-3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.2-2
- Rebuild for boost 1.57.0

* Tue Jan  6 2015 Peng Wu <pwu@redhat.com> - 1.2-1
- Update to 1.2

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.1-4
- Rebuild for boost 1.55.0

* Thu May 22 2014 Brent Baude <baude@us.ibm.com> - 1.1-3
- FTBFS on all arches due to missing gflags.h
- Adding BR for gflags-devel 

* Mon Dec 30 2013 Peng Wu <pwu@redhat.com> - 1.1-2
- Update arm patch

* Fri Dec 27 2013 Peng Wu <pwu@redhat.com> - 1.1-1
- Update to 1.1

* Mon Dec  9 2013 Peng Wu <pwu@redhat.com> - 1.0-1
- Update to 1.0

* Mon Nov 25 2013 Peng Wu <pwu@redhat.com> - 0.9.9-1
- Update to 0.9.9

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.9.8-4
- Rebuild for boost 1.54.0

* Mon Jul 15 2013 Peng Wu <pwu@redhat.com> - 0.9.8-3
- Fixes arm build

* Thu May 16 2013 Peng Wu <pwu@redhat.com> - 0.9.8-2
- Improves the spec

* Thu May  9 2013 Peng Wu <pwu@redhat.com> - 0.9.8-1
- The Initial Version

