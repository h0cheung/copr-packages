%global build_timestamp %(date +"%Y%m%d")
%global forgeurl https://github.com/choff/anbox-modules
%global branch   master

%forgemeta

Name:           ashmem-dkms
Version:        git
Release:        1%{?dist}
Summary:        DKMS Kernel modules ashmem_linux

License:        GPL
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

Requires:       dkms
Requires:       systemd-udev
%{?systemd_requires}

BuildRequires:	systemd

Requires(posttrans): dkms
Requires(preun):  dkms

%description
ashmem_linux module for waydroid and anbox.

%prep
%forgesetup

%build

%install
install -dm 755 %{buildroot}%{_udevrulesdir}
cat > %{buildroot}%{_udevrulesdir}/99-anbox.rules << EOF
KERNEL=="ashmem", NAME="%k", MODE="0666"
EOF
chmod 644 %{buildroot}%{_udevrulesdir}/99-anbox.rules

install -dm 755 %{buildroot}%{_usrsrc}
cp -rT ashmem %{buildroot}%{_usrsrc}/anbox-ashmem-1

%check

%files
%defattr(-,root,root,-)
%{_udevrulesdir}/99-anbox.rules
%{_usrsrc}/anbox-ashmem-1/

%posttrans
%udev_rules_update
dkms install anbox-ashmem/1

%preun
dkms remove anbox-ashmem/1 --all

%postun
%udev_rules_update


%changelog
* Tue Jun 07 2022 Howard Cheung <mail@h-cheung.cf>
- Initial build
