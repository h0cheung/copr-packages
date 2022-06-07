%global build_timestamp %(date +"%Y%m%d")
%global forgeurl https://github.com/GNOME/libshumate
Version:        1.0.0.alpha.1
%global tag     %{version}

%forgemeta

Name:           libshumate
Release:        1%{?dist}
Summary:        A GTK4 widget to display maps

License:        LGPLv2.1
URL:            https://wiki.gnome.org/Projects/libshumate
Source0:        %{forgesource}

BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(gi-docgen)

%description
libshumate is a GTK4 widget to display maps.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%forgesetup

%build
%meson -Dlibsoup3=true
%meson_build

%install
%meson_install

%check

%files
%license COPYING
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*
%{_datadir}/gir-1.0/*
%{_datadir}/vala/vapi/*

%files devel
%doc %{_datadir}/doc/libshumate-1.0/*
%license COPYING
/usr/include/shumate-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
%autochangelog
