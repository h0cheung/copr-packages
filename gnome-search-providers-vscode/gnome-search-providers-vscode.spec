%global forgeurl         https://codeberg.org/flausch/gnome-search-providers-vscode
Version:                 1.9.1
%global debug_package    %{nil}

%forgemeta

Name:                    gnome-search-providers-vscode
Release:                 1%{?dist}
Summary:                 Add recent workspaces of various VSCode variants to Gnome search.

License:                 MPL 2
URL:                     %{forgeurl}
Source0:                 %{forgeurl}/archive/v%{version}.tar.gz

BuildRequires:           rust >= 1.50
BuildRequires:           cargo
BuildRequires:           glib2-devel
BuildRequires:           make
BuildRequires:           rust-libsystemd-devel
BuildRequires:           systemd-libs
BuildRequires:           systemd-devel
BuildRequires:           rust-libsystemd+default-devel

Requires:		 gnome-shell

%description             
Supports:
 ---
 Code OSS (Arch Linux)
 VSCodium
 Visual Studio Code (AUR package)
 Visual Studio Code (Official packages)
 ---
Under the hood this is a small systemd user service which implements the search provider DBus API and exposes recent workspaces from VSCode

%prep
%autosetup -n %{name}

%define my_cmake_flags PREFIX=/usr DATADIR=%{buildroot}%{_datadir} LIBDIR=%{buildroot}%{_libdir}

%build
%make_build %{my_cmake_flags}

%install
%make_install %{my_cmake_flags}

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%{_libdir}/%{name}/%{name}
%{_userunitdir}/%{name}.service
%{_datadir}/dbus-1/services/de.swsnr.searchprovider.VSCode.service
%{_datadir}/share/gnome-shell/search-providers/de.swsnr.searchprovider.vscode.arch.code-oss.ini
%{_datadir}/share/gnome-shell/search-providers/de.swsnr.searchprovider.vscode.arch.visual-studio-code.ini
%{_datadir}/share/gnome-shell/search-providers/de.swsnr.searchprovider.vscode.codium.ini
%{_datadir}/share/gnome-shell/search-providers/de.swsnr.searchprovider.vscode.official.code.ini


%changelog
%autochangelog
