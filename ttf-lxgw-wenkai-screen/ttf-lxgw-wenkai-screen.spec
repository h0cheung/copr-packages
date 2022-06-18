Name:           ttf-lxgw-wenkai-screen
Version:        %(api_result=$(curl -s https://api.github.com/repos/lxgw/LxgwWenKai-Screen/tags | head -n 3 | tail -n 1); echo $api_result | grep -oP '(?<="v).*(?=",)')
Release:        1%{?dist}
Summary:        An open-source Chinese font derived from Fontworks' Klee One, for screen reading
License:        OFL-1.1
Url:            https://github.com/lxgw/LxgwWenKai-Screen
Source0:        %{url}/releases/download/v%{version}/LXGWWenKaiScreen.ttf
Source1:        %{url}/releases/download/v%{version}/LXGWWenKaiScreenR.ttf
Source2:        https://github.com/lxgw/LxgwWenKai/raw/main/License.txt
BuildRequires:  fontpackages-devel
BuildArch:      noarch

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

%description
%{summary}.

%prep
%define _ttfontsdir /usr/share/fonts/lxgw-wenkai-screen

%build

%install
install -d %{buildroot}%{_ttfontsdir}
# by default install command uses 755 umask
install -m 644 %{S:0} %{S:1} %{buildroot}%{_ttfontsdir}

%post
%postun

%files
%license %{S:2}
%{_ttfontsdir}/*.ttf
%dir %{_ttfontsdir}

%changelog
