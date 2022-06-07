# Generated by go2rpm 1.6.0, based on clash.spec in official repo.
%bcond_without check
%global build_timestamp %(date +"%Y%m%d")

# https://github.com/MetaCubeX/Clash.Meta
%global goipath         github.com/MetaCubeX/Clash.Meta
%global tag             Alpha

%gometa

%global common_description %{expand:
A rule-based tunnel in Go.}

%global golicenses      LICENSE
%global godocs          docs README.md

Name:           clash-meta-modified
Version:        Alpha
Release:        %autorelease
Summary:        A rule-based tunnel in Go
Provides:       clash
Conflicts:      clash

License:        GPLv3
URL:            %{gourl}
Source0:        %{gosource}
Source1:        clash.service
Source2:        clash@.service

BuildRequires:  systemd-rpm-macros
BuildRequires:  git

%undefine _missing_build_ids_terminate_build
%global debug_package %{nil}

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1
sed "s/unknown version/${pkgver}/" -i constant/version.go
sed "s/unknown time/$(LANG=C date -u)/" -i constant/version.go
chmod -x docs/logo.png

%build
go build -o %{gobuilddir}/bin/clash .

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vd                     %{buildroot}%{_userunitdir}
install -m 0755 -vd                     %{buildroot}%{_unitdir}

install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vp %{S:1}              %{buildroot}%{_userunitdir}/
install -m 0755 -vp %{S:2}              %{buildroot}%{_unitdir}/


%if %{with check}
%check
%gocheck ||:
%endif

%post
%systemd_user_post clash.service
%systemd_post clash@.service

%preun
%systemd_user_preun clash.service
# disable --now seems don't work here.
if [ $1 -eq 0 ] && [ -x /usr/bin/systemctl ] ; then
        # Package removal, not upgrade
        /usr/bin/systemctl --no-reload stop clash@*.service || :
        /usr/bin/systemctl --no-reload disable clash@.service || :
fi

%postun
%systemd_user_postun_with_restart clash.service
%systemd_postun_with_restart clash@*.service


%files
%license LICENSE
%doc docs README.md
%{_bindir}/clash
%{_userunitdir}/clash.service
%{_unitdir}/clash@.service
%gopkgfiles

%changelog
%autochangelog
