%global toolchain               clang
%global forgeurl                https://gitlab.com/famedly/fluffychat
Version:                        1.3.1
%global tag                     v%{version}

%forgemeta

Name:            fluffychat
Release:         1%{?dist}
Summary:         Chat with your friends
License:         AGPLv3
URL:             %{forgeurl}

Source0:         %{forgesource}
Source1:         https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_2.10.4-stable.tar.xz
Source2:         https://github.com/be5invis/Sarasa-Gothic/releases/download/v0.36.2/sarasa-gothic-ttf-0.36.2.7z

BuildRequires:   cmake
BuildRequires:   git
BuildRequires:   clang compiler-rt
BuildRequires:   ninja-build
BuildRequires:   make
BuildRequires:   webkit2gtk3-devel
BuildRequires:   jsoncpp-devel
BuildRequires:   libsecret-devel
BuildRequires:   libolm-devel
BuildRequires:   chrpath
BuildRequires:   p7zip-plugins

Requires:        jsoncpp
Requires:        libsecret
Requires:        libolm

%description
%{summary}.

%prep
%forgeautosetup
7z e %{S:2}
tar -xoaf%{S:1}


%build
./flutter/bin/flutter config --no-analytics
./flutter/bin/flutter config --enable-linux-desktop
./flutter/bin/flutter clean
./flutter/bin/flutter pub get
./flutter/bin/flutter build linux --release --verbose
chrpath --delete build/linux/x64/release/bundle/lib/*
mv -f sarasa-gothic-sc-regular.ttf build/linux/x64/release/bundle/data/flutter_assets/fonts/Roboto/Roboto-Regular.ttf
mv -f sarasa-gothic-sc-bold.ttf build/linux/x64/release/bundle/data/flutter_assets/fonts/Roboto/Roboto-Bold.ttf
mv -f sarasa-gothic-sc-italic.ttf build/linux/x64/release/bundle/data/flutter_assets/fonts/Roboto/Roboto-Italic.ttf

%install
install -dm755 %{buildroot}/opt
mv build/linux/x64/release/bundle %{buildroot}/opt/%{name}
install -dm755 %{buildroot}%{_bindir}
ln -s /opt/%{name}/%{name} %{buildroot}%{_bindir}/%{name}
# icon
install -Dm 644 %{buildroot}/opt/%{name}/data/flutter_assets/assets/favicon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
# desktop entry

install -dm 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Version=%{version}
Name=FluffyChat
Comment=Matrix Client. Chat with your friends
Exec=%{name}
Icon=%{name}
Terminal=false
EOF

%files
%license LICENSE
%doc README.md
/opt/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}

%changelog
