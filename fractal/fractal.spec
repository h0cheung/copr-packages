%define build_date %(date +"%Y%m%d")

%global forgeurl https://github.com/GNOME/fractal/tree/master
%global branch   main

%forgemeta

%global appname fractal
%global uuid    org.gnome.Fractal

Name:           %{appname}
Version:        git
Release:        1%{?dist}
Summary:        Matrix messaging app for GNOME written in Rust

License:        GPLv3+
URL:            https://gitlab.gnome.org/GNOME/fractal
Source0:        %{forgesource}

BuildRequires:  cargo
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  clang-devel
BuildRequires:  gmp-devel
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  rust

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-player-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(shumate-1.0)

Requires:       hicolor-icon-theme

%description
Fractal is a Matrix messaging app for GNOME written in Rust. Its interface is
optimized for collaboration in large groups, such as free software projects

%prep
%forgeautosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appname}

%files -f %{appname}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/%{appname}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml

%changelog
%autochangelog
