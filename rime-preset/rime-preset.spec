%global build_timestamp %(date +"%Y%m%d")
%global forgeurl        https://github.com/rime/plum
%global branch          master
%global debug_package   %{nil}

%forgemeta

Name:           rime-preset
Version:        git
Release:        1%{?dist}
Provides:       brise = 0.38
Obsoletes:      brise
Conflicts:      brise
Summary:        The official Rime schema repository
License:        GPLv3
URL:            %{forgeurl}
Source:         %{forgesource}

Buildrequires:  git
Buildrequires:  make
BuildRequires:  librime-tools

%description
La brise: The official Rime schema repository.

%prep
%forgesetup


%build
%make_build
%make_build build

%install
%make_install


%files
%license LICENSE
%doc README.md
%{_datadir}/rime-data/**


%changelog

