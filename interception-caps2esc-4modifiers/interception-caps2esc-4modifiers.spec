%bcond_without check
%define build_date %(date +"%Y%m%d")

%global forgeurl https://gitlab.com/h-cheung/caps2esc
%global branch   master

%forgemeta

Name:           interception-caps2esc-4modifiers
Version:        git
Release:        1%{?dist}
Summary:        Transforming the most useless key ever in the most useful one.

License:        MIT
URL:	 %{forgeurl}
Source:  %{forgesource}

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: kernel-headers
BuildRequires: cmake
Requires:      interception-tools

%description
Transforming the most useless key ever in the most useful one.
For vi/Vim/NeoVim addicts at least.

%prep
%forgesetup

%build
%cmake
%cmake_build

%install
rm -rf $RPM_BUILD_ROOT
%cmake_install 

%files
%license LICENSE.md
%doc README.md
%{_bindir}/*

%changelog
