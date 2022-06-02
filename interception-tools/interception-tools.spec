%bcond_without check
%global build_timestamp %(date +"%Y%m%d")

%global forgeurl https://gitlab.com/interception/linux/tools.git
%global branch   master

%forgemeta

Name:           interception-tools
Version:        git
Release:        1%{?dist}
Summary:        A minimal composable infrastructure on top of libudev and libevdev

License:        GPLv3+
URL:	 %{forgeurl}
Source0:  https://gitlab.com/interception/linux/tools/-/archive/master/tools-master.tar.bz2
Source1:  udevmon.service

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libevdev-devel
BuildRequires: systemd-devel
BuildRequires: systemd-rpm-macros
BuildRequires: yaml-cpp-devel

%description
The Interception Tools is a small set of utilities for operating on input
events of evdev devices.

%prep
%autosetup -n tools-master

%build
%cmake
%cmake_build

%install
rm -rf $RPM_BUILD_ROOT
%cmake_install

install -Dm644 %{S:1} $RPM_BUILD_ROOT%{_unitdir}/udevmon.service

%preun
%systemd_preun udevmon.service

%postun
%systemd_postun_with_restart udevmon.service

%files
%license LICENSE.md
%doc README.md
%{_bindir}/*
%{_unitdir}/udevmon.service

%changelog

