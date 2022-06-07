%global forgeurl         https://codeberg.org/flausch/gnome-search-providers-jetbrains
Version:                 1.11.2
%global debug_package    %{nil}

%forgemeta

Name:                    gnome-search-providers-jetbrains
Release:                 1%{?dist}
Summary:                 Add recent projects of various Jetbrains IDEs to Gnome search.

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
 Android Studio (toolbox)
 CLion (toolbox)
 GoLand (toolbox)
 IDEA (toolbox)
 IDEA Community Edition (toolbox)
 PHPStorm (toolbox)
 PyCharm (toolbox)
 Rider (toolbox)
 RubyMine (toolbox)
 WebStorm (toolbox)
 ---
Under the hood, this is a small systemd user service that implements the search 
provider DBus API and exposes recent projects from Jetbrains IDEs
%prep
%autosetup -n %{name}

%build
%make_build

%install
%make_install PREFIX=/usr DATADIR=%{_datadir} LIBEXECDIR=%{_libexecdir}/%{name} USERUNITDIR=%{_userunitdir}


%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%{_libexecdir}/%{name}/%{name}
%{_userunitdir}/%{name}.service
%{_datadir}/dbus-1/services/de.swsnr.searchprovider.Jetbrains.service
%{_datadir}/gnome-shell/search-providers/de.swsnr.searchprovider.jetbrains.toolbox.clion.ini
%{_datadir}/gnome-shell/search-providers/de.swsnr.searchprovider.jetbrains.toolbox.goland.ini
%{_datadir}/gnome-shell/search-providers/de.swsnr.searchprovider.jetbrains.toolbox.idea-ce.ini
%{_datadir}/gnome-shell/search-providers/de.swsnr.searchprovider.jetbrains.toolbox.idea.ini
%{_datadir}/gnome-shell/search-providers/de.swsnr.searchprovider.jetbrains.toolbox.phpstorm.ini
%{_datadir}/gnome-shell/search-providers/de.swsnr.searchprovider.jetbrains.toolbox.pycharm.ini
%{_datadir}/gnome-shell/search-providers/de.swsnr.searchprovider.jetbrains.toolbox.rider.ini
%{_datadir}/gnome-shell/search-providers/de.swsnr.searchprovider.jetbrains.toolbox.rubymine.ini
%{_datadir}/gnome-shell/search-providers/de.swsnr.searchprovider.jetbrains.toolbox.studio.ini
%{_datadir}/gnome-shell/search-providers/de.swsnr.searchprovider.jetbrains.toolbox.webstorm.ini


%changelog
%autochangelog
