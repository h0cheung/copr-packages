Name:           sarasa-gothic-fonts
Version:        %(api_result=$(curl -s https://api.github.com/repos/be5invis/Sarasa-Gothic/tags | head -n 3 | tail -n 1); echo ${api_result:14:6})
Release:        1%{?dist}
Summary:        SARASA GOTHIC, a CJK programing font based on Iosevka, Inter and Source Han Sans
License:        OFL-1.1
Url:            https://github.com/be5invis/Sarasa-Gothic
Source0:        https://github.com/be5invis/Sarasa-Gothic/releases/download/v%{version}/sarasa-gothic-ttc-%{version}.7z
Source1:        https://raw.githubusercontent.com/be5invis/Sarasa-Gothic/master/LICENSE
BuildRequires:  fontpackages-devel
BuildRequires:  p7zip
BuildArch:      noarch

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

%description
SARASA GOTHIC, a CJK programming font based on Iosevka, Inter and Source Han Sans.

%prep
%setup -qcn %{name}-%{version}
cp %{S:1} ./
%define _ttfontsdir /usr/share/fonts/sarasa-gothic

%build

%install
install -d %{buildroot}%{_ttfontsdir}
# by default install command uses 755 umask
install -m 644 *.ttc %{buildroot}%{_ttfontsdir}

%post
%postun

%files
%license LICENSE
%{_ttfontsdir}/*.ttc
%dir %{_ttfontsdir}

%changelog
