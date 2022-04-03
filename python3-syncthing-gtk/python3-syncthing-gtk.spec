%bcond_without check
%define build_date %(date +"%Y%m%d")

%global forgeurl https://github.com/andrewshadura/syncthing-gtk
%global branch   main

%forgemeta

Name:           python3-syncthing-gtk
Summary:        Syncthing GTK+ GUI
Version:        git
Release:        1%{?dist}
License:        GPLv2
URL:	        %{forgeurl}
Source:         %{forgesource}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  desktop-file-utils
BuildRequires:  gettext

BuildArch:      noarch

Requires:       syncthing >= 0.12
Requires:       hicolor-icon-theme

Requires:       psmisc
Requires:       python3-dateutil
Requires:       python3-gobject
Requires:       python3-bcrypt
Provides:       syncthing-gtk
Conflicts:       syncthing-gtk

%if 0%{?fedora}
Recommends:     python-inotify
%else
Requires:       python-inotify
%endif


%description
Syncthing replaces Dropbox and BitTorrent Sync with something open,
trustworthy and decentralized. Your data is your data alone and you
deserve to choose where it is stored, if it is shared with some third
party and how it's transmitted over the Internet.

Using syncthing, that control is returned to you.

This package contains the GTK+ GUI for syncthing.


%prep
%forgesetup


%build
%py3_build


%install
sh generate-locales.sh
%py3_install
%find_lang syncthing-gtk


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/syncthing-gtk.desktop || :


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f syncthing-gtk.lang
%license LICENSE

%{_bindir}/syncthing-gtk

%{_datadir}/applications/syncthing-gtk.desktop

%{_datadir}/icons/hicolor/*/*/*.png

%{_datadir}/pixmaps/syncthing-gtk.png
%{_datadir}/syncthing-gtk/

%{_mandir}/man1/syncthing-gtk.1.gz

%{python3_sitelib}/syncthing_gtk-*.egg-info
%{python3_sitelib}/syncthing_gtk/

%{_datadir}/metainfo/me.kozec.syncthingtk.appdata.xml


%changelog


