%global build_timestamp %(date +"%Y%m%d")
%global forgeurl        https://github.com/so1ar/rime-cloverpinyin
%global branch          main

%forgemeta

Name:           rime-cloverpinyin
Version:        git
Release:        1%{?dist}
Summary:        A RIME zh_CN pinyin schema, fork by so1ar.
License:        LGPLv3
Url:            %{forgeurl}
Source:         %{forgesource}
Patch0:         no_pypinyin_dict.patch
BuildArch:      noarch
Recommends:     librime
Buildrequires:  bash
Buildrequires:  librime-tools
Buildrequires:  opencc-tools
Buildrequires:  python python-devel python-pip python-requests python-setuptools
Buildrequires:  aria2
Buildrequires:  git
Buildrequires:  rime-preset

%description
A RIME zh_CN pinyin schema, fork by so1ar.

%prep
%forgesetup
%patch0 -p1

%build
pip install jieba opencc pypinyin
bash -c "LANG=C.UTF-8 bash build"

%install
cd data
install -Dm644 *.yaml -t %{buildroot}%{_datadir}/rime-data/
install -Dm644 opencc/* -t %{buildroot}%{_datadir}/rime-data/opencc
install -Dm644 build/* -t %{buildroot}%{_datadir}/rime-data/build

%post
%postun

%files
%license LICENSE
%doc README.md
%{_datadir}/rime-data/**

%changelog
