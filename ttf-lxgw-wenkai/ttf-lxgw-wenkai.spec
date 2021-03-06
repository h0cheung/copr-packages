Name:           ttf-lxgw-wenkai
Version:        %(api_result=$(curl -s https://api.github.com/repos/lxgw/LxgwWenKai/tags | head -n 3 | tail -n 1); echo $api_result | grep -oP '(?<="v).*(?=",)')
Release:        1%{?dist}
Summary:        An open-source Chinese font derived from Fontworks' Klee One
License:        OFL-1.1
Url:            https://github.com/lxgw/LxgwWenKai
Source0:        %{url}/releases/download/v%{version}/lxgw-wenkai-v%{version}.tar.gz
BuildRequires:  fontpackages-devel
BuildArch:      noarch

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

%description
%{summary}.

%prep
%setup -qn lxgw-wenkai-v%{version}
%define _ttfontsdir /usr/share/fonts/lxgw-wenkai

%build

%install
install -d %{buildroot}%{_ttfontsdir}
# by default install command uses 755 umask
install -m 644 *.ttf %{buildroot}%{_ttfontsdir}

%post
%postun

%files
%license License.txt
%{_ttfontsdir}/*.ttf
%dir %{_ttfontsdir}

%changelog
