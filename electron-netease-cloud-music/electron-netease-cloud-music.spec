%global debug_package %{nil}
%global forgeurl https://github.com/Rocket1184/electron-netease-cloud-music
Version:        0.9.34

%forgemeta

Name:           electron-netease-cloud-music
Release:        1%{?dist}
Summary:        UNOFFICIAL client for music.163.com . Powered by Electron, Vue, and Muse-UI
License:        GPLv3
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        electron-netease-cloud-music.sh
Source2:        electron-netease-cloud-music.desktop

Requires:       electron
BuildRequires:  yarnpkg

%description
%{summary}.

%prep
%forgesetup

%build
yarn install --ignore-scripts
yarn dist

%install
install -d %{buildroot}%{_prefix}/lib/
cp -r dist %{buildroot}%{_prefix}/lib/electron-netease-cloud-music
install -Dm755 %{S:1} %{buildroot}%{_bindir}/electron-netease-cloud-music
install -Dm644 %{S:2} -t %{buildroot}%{_datadir}/applications/
install -Dm644 assets/icons/icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/electron-netease-cloud-music.svg

%files
%license LICENSE
%doc README.md
%{_bindir}/electron-netease-cloud-music
%{_prefix}/lib/electron-netease-cloud-music/
%{_datadir}/applications/electron-netease-cloud-music.desktop
%{_datadir}/icons/hicolor/scalable/apps/electron-netease-cloud-music.svg

%changelog
