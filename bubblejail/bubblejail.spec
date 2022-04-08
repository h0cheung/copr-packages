Name:           bubblejail
Version:        0.5.2
Release:        1%{?dist}
Summary:        Bubblewrap based sandboxing for desktop applications

License:        GPLv3+
URL:            https://github.com/igo95862/bubblejail
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
Patch0:         ca_path_fix.patch

BuildRequires:  meson
BuildRequires:  m4
BuildRequires:  python3-sphinx
Requires:       python3 >= 3.8
Requires:       python3-pyxdg
Requires:       python3-tomli
Requires:       python3-tomli-w
Requires:       python3-qt5-base
Requires:       desktop-file-utils
Requires:       bubblewrap
Requires:       xdg-dbus-proxy

%undefine _debugsource_packages

%description
Bubblejail is a bubblewrap-based alternative to Firejail.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md docs/breaking_changes.md
%_bindir/bubblejail
%_bindir/bubblejail-config
%_libdir/bubblejail
%_datadir/applications/bubblejail-config.desktop
%_datadir/bash-completion/completions/bubblejail
%_datadir/bubblejail
%_datadir/fish/vendor_completions.d/bubblejail.fish
%_datadir/icons/hicolor/48x48/apps/bubblejail-config.png
%_datadir/icons/hicolor/scalable/apps/bubblejail-config.svg
%_mandir/man1/bubblejail.1.gz


%changelog
