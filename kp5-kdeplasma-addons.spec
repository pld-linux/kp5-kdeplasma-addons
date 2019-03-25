%define		kdeplasmaver	5.15.3
%define		qtver		5.9.0
%define		kpname		kdeplasma-addons

Summary:	All kind of addons to improve your Plasma experience
Name:		kp5-%{kpname}
Version:	5.15.3
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	a1b032662fd6267b7bf0e8a0ff627db0
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	glib2-devel
BuildRequires:	ibus-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdesignerplugin-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kinit-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-kparts-devel
BuildRequires:	kf5-kross-devel
BuildRequires:	kf5-kross-devel
BuildRequires:	kf5-krunner-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-kunitconversion-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	libxcb-devel
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	scim-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
All kind of addons to improve your Plasma experience.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
/etc/xdg/comic.knsrc
#%attr(755,root,root) %{_libdir}/kimpanel-ibus-panel
#%attr(755,root,root) %{_libdir}/kimpanel-scim-panel
%attr(755,root,root) %ghost %{_libdir}/libplasmacomicprovidercore.so.1
%attr(755,root,root) %{_libdir}/libplasmacomicprovidercore.so.*.*.*
#%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_krunner_audioplayercontrol.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_krunner_dictionary.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_krunner_spellcheck.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_comic.so
#%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_audioplayercontrol.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_converter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_datetime.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_dictionary.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_spellcheck.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/applets/plasma_applet_comic.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_comic.so
#%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_kimpanel.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_konsoleprofiles.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma_comic_krossprovider.so
#%dir %{_libdir}/qt5/qml/org/kde/plasma/private/activitypager
#%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/activitypager/libactivitypagerplugin.so
#%{_libdir}/qt5/qml/org/kde/plasma/private/activitypager/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/colorpicker
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/colorpicker/libcolorpickerplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/colorpicker/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/diskquota
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/diskquota/libdiskquotaplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/diskquota/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/quicklaunch
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/quicklaunch/libquicklaunchplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/quicklaunch/qmldir

%dir %{_libdir}/qt5/qml/org/kde/plasma/private/fifteenpuzzle
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/fifteenpuzzle/libfifteenpuzzleplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/fifteenpuzzle/qmldir
#%dir %{_libdir}/qt5/qml/org/kde/plasma/private/kimpanel
#%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/kimpanel/libkimpanelplugin.so
#%{_libdir}/qt5/qml/org/kde/plasma/private/kimpanel/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/notes
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/notes/libnotesplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/notes/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/showdesktop
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/showdesktop/libshowdesktopplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/showdesktop/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/timer
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/timer/libtimerplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/timer/qmldir
%{_iconsdir}/hicolor/scalable/apps/fifteenpuzzle.svgz
%{_datadir}/kservices5/kwin/kwin4_desktop_switcher_previews.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_big_icons.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_compact.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_informative.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_present_windows.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_small_icons.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_text.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_thumbnails.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.calculator.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.comic.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.fifteenpuzzle.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.fuzzyclock.desktop
#%%{_datadir}/kservices5/plasma-applet-org.kde.plasma.kickerdash
#%{_datadir}/kservices5/plasma-applet-org.kde.plasma.kimpanel.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.konsoleprofiles.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.notes.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.showdesktop.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.systemloadviewer.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.timer.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.webbrowser.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.activitypager.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.colorpicker.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.diskquota.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.kickerdash.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.quicklaunch.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.userswitcher.desktop
%{_datadir}/kservices5/plasma-dataengine-comic.desktop
#%{_datadir}/kservices5/plasma-dataengine-kimpanel.desktop
%{_datadir}/kservices5/plasma-dataengine-konsoleprofiles.desktop
#%{_datadir}/kservices5/plasma-runner-audioplayercontrol.desktop
#%{_datadir}/kservices5/plasma-runner-audioplayercontrol_config.desktop
%{_datadir}/kservices5/plasma-runner-converter.desktop
%{_datadir}/kservices5/plasma-runner-datetime.desktop
%{_datadir}/kservices5/plasma-runner-dictionary.desktop
%{_datadir}/kservices5/plasma-runner-dictionary_config.desktop
%{_datadir}/kservices5/plasma-runner-spellchecker.desktop
%{_datadir}/kservices5/plasma-runner-spellchecker_config.desktop
%{_datadir}/kservices5/plasma-wallpaper-org.kde.haenau.desktop
%{_datadir}/kservices5/plasma-wallpaper-org.kde.hunyango.desktop
%{_datadir}/kservicetypes5/plasma_comicprovider.desktop
%{_datadir}/kwin/desktoptabbox
%{_datadir}/kwin/tabbox
#%%{_datadir}/plasma/desktoptheme/default/widgets/notes.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/timer.svgz
%{_datadir}/plasma/plasmoids/org.kde.plasma.calculator
%{_datadir}/plasma/plasmoids/org.kde.plasma.comic
%{_datadir}/plasma/plasmoids/org.kde.plasma.fifteenpuzzle
%{_datadir}/plasma/plasmoids/org.kde.plasma.fuzzyclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickerdash
#%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel
%{_datadir}/plasma/plasmoids/org.kde.plasma.konsoleprofiles
%{_datadir}/plasma/plasmoids/org.kde.plasma.notes
%{_datadir}/plasma/plasmoids/org.kde.plasma.showdesktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemloadviewer
%{_datadir}/plasma/plasmoids/org.kde.plasma.timer
%{_datadir}/plasma/plasmoids/org.kde.plasma.webbrowser
%{_datadir}/plasma/desktoptheme/default/icons/quota.svg
#%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager
#%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager/contents
#%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager/contents/code
#%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager/contents/config
#%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager/contents/ui
#%{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager/contents/code/utils.js
#%{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager/contents/config/config.qml
#%{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager/contents/config/main.xml
#%{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager/contents/ui/configGeneral.qml
#%{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager/contents/ui/main.qml
#%{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager/metadata.desktop
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.colorpicker
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.colorpicker/contents
#%%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.colorpicker/contents/code
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.colorpicker/contents/config
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.colorpicker/contents/ui
#%%{_datadir}/plasma/plasmoids/org.kde.plasma.colorpicker/contents/code/logic.js
%{_datadir}/plasma/plasmoids/org.kde.plasma.colorpicker/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.colorpicker/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.colorpicker/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.colorpicker/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.colorpicker/metadata.desktop
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.diskquota
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.diskquota/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.diskquota/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.diskquota/contents/ui/ListDelegateItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.diskquota/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.diskquota/metadata.desktop
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch/contents
#%%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/code
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/config
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/ui
#%%{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/code/layout.js
%{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/ui/ConfigGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/ui/IconItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/ui/Popup.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/ui/UrlModel.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch/metadata.desktop
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.userswitcher
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.userswitcher/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.userswitcher/contents/config
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.userswitcher/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.userswitcher/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.userswitcher/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.userswitcher/contents/ui/ListDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.userswitcher/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.userswitcher/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.userswitcher/metadata.desktop
#%{_datadir}/plasma/services/kimpanel.operations
%{_datadir}/plasma/services/org.kde.plasma.dataengine.konsoleprofiles.operations
%{_datadir}/plasma/wallpapers/org.kde.haenau
%{_datadir}/plasma/wallpapers/org.kde.hunyango

%{_libdir}/libplasmapotdprovidercore.so
%ghost %{_libdir}/libplasmapotdprovidercore.so.1
%{_libdir}/libplasmapotdprovidercore.so.1.*.*
#%%ghost %{_libdir}/libplasmaweather.so.1
#%%{_libdir}/libplasmaweather.so.2.*.*
%{_libdir}/qt5/plugins/krunner_katesessions.so
%{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.grouping.so
%{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.private.grouping.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_weather.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_potd.so
%dir %{_libdir}/qt5/plugins/potd
%{_libdir}/qt5/plugins/potd/plasma_potd_apodprovider.so
%{_libdir}/qt5/plugins/potd/plasma_potd_bingprovider.so
%{_libdir}/qt5/plugins/potd/plasma_potd_epodprovider.so
%{_libdir}/qt5/plugins/potd/plasma_potd_flickrprovider.so
%{_libdir}/qt5/plugins/potd/plasma_potd_natgeoprovider.so
%{_libdir}/qt5/plugins/potd/plasma_potd_noaaprovider.so
%{_libdir}/qt5/plugins/potd/plasma_potd_wcpotdprovider.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/mediaframe
%{_libdir}/qt5/qml/org/kde/plasma/private/mediaframe/libmediaframeplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/mediaframe/qmldir
#%%dir %{_libdir}/qt5/qml/org/kde/plasma/private/minimizeall
#%%{_libdir}/qt5/qml/org/kde/plasma/private/minimizeall/libminimizeallplugin.so
#%%{_libdir}/qt5/qml/org/kde/plasma/private/minimizeall/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/purpose
%{_libdir}/qt5/qml/org/kde/plasma/private/purpose/libpurposeplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/purpose/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/weather
%{_libdir}/qt5/qml/org/kde/plasma/private/weather/libweatherplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/weather/qmldir
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.binaryclock.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.grouping.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.mediaframe.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.minimizeall.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.private.grouping.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.quickshare.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.weather.desktop
%{_datadir}/kservices5/plasma-dataengine-potd.desktop
%{_datadir}/kservices5/plasma-runner-katesessions.desktop
%{_datadir}/kservices5/plasma-wallpaper-org.kde.potd.desktop
%{_datadir}/metainfo/org.kde.haenau.appdata.xml
%{_datadir}/metainfo/org.kde.hunyango.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.activitypager.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.binaryclock.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.calculator.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.colorpicker.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.comic.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.diskquota.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.fifteenpuzzle.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.fuzzyclock.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.grouping.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.kickerdash.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.konsoleprofiles.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mediaframe.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.minimizeall.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.notes.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicklaunch.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quickshare.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.showdesktop.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemloadviewer.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.timer.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.userswitcher.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.weather.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.webbrowser.appdata.xml
%{_datadir}/metainfo/org.kde.potd.appdata.xml
%dir %{_datadir}/plasma/desktoptheme/default/weather
%{_datadir}/plasma/desktoptheme/default/weather/wind-arrows.svgz
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.binaryclock
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.binaryclock/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.binaryclock/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.binaryclock/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.binaryclock/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.binaryclock/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.binaryclock/contents/ui/BinaryClock.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.binaryclock/contents/ui/Dot.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.binaryclock/contents/ui/DotColumn.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.binaryclock/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.binaryclock/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.binaryclock/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.binaryclock/metadata.json

%{_datadir}/plasma/plasmoids/org.kde.plasma.colorpicker/metadata.json

%{_datadir}/plasma/plasmoids/org.kde.plasma.diskquota/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.grouping
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.grouping/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.grouping/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.grouping/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.grouping/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.grouping/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.mediaframe
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.mediaframe/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.mediaframe/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediaframe/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediaframe/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.mediaframe/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediaframe/contents/ui/ConfigGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediaframe/contents/ui/ConfigPaths.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediaframe/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediaframe/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediaframe/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.grouping
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.grouping/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.grouping/contents/applet
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.grouping/contents/applet/CompactApplet.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.grouping/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.grouping/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.grouping/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.grouping/contents/ui
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.grouping/contents/ui/items
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.grouping/contents/ui/items/AbstractItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.grouping/contents/ui/items/PlasmoidItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.grouping/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.grouping/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.grouping/metadata.json

%{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.quickshare
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.quickshare/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.quickshare/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.quickshare/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.quickshare/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.quickshare/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.quickshare/contents/ui/PasteMenuItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.quickshare/contents/ui/ShareDialog.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.quickshare/contents/ui/ShowUrlDialog.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.quickshare/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.quickshare/contents/ui/settingsGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.quickshare/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.quickshare/metadata.json

%{_datadir}/plasma/plasmoids/org.kde.plasma.userswitcher/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.weather
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/config/config.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/DetailsView.qml
#%%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/FiveDaysView.qml
#%%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/Notice.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/NoticesView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/TopPanel.qml
#%%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/WeatherListView.qml
#%%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/configUnits.qml
#%%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/configWeatherStation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/metadata.json
%dir %{_datadir}/plasma/wallpapers/org.kde.potd
%dir %{_datadir}/plasma/wallpapers/org.kde.potd/contents
%dir %{_datadir}/plasma/wallpapers/org.kde.potd/contents/config
%{_datadir}/plasma/wallpapers/org.kde.potd/contents/config/main.xml
%dir %{_datadir}/plasma/wallpapers/org.kde.potd/contents/ui
%{_datadir}/plasma/wallpapers/org.kde.potd/contents/ui/config.qml
%{_datadir}/plasma/wallpapers/org.kde.potd/contents/ui/main.qml
%{_datadir}/plasma/wallpapers/org.kde.potd/metadata.desktop
%{_datadir}/plasma/wallpapers/org.kde.potd/metadata.json

%{_libdir}/qt5/plugins/kcm_krunner_charrunner.so
%{_libdir}/qt5/plugins/krunner_charrunner.so
%{_libdir}/qt5/plugins/krunner_konsoleprofiles.so
%{_libdir}/qt5/plugins/plasmacalendarplugins/astronomicalevents.so
%dir %{_libdir}/qt5/plugins/plasmacalendarplugins/astronomicalevents
%{_libdir}/qt5/plugins/plasmacalendarplugins/astronomicalevents/AstronomicalEventsConfig.qml
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/dict
%{_libdir}/qt5/qml/org/kde/plasma/private/dict/libdictplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/dict/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasmacalendar
%dir %{_libdir}/qt5/qml/org/kde/plasmacalendar/astronomicaleventsconfig
%{_libdir}/qt5/qml/org/kde/plasmacalendar/astronomicaleventsconfig/libplasmacalendarastronomicaleventsconfig.so
%{_libdir}/qt5/qml/org/kde/plasmacalendar/astronomicaleventsconfig/qmldir
%{_iconsdir}/hicolor/scalable/apps/accessories-dictionary.svgz
%{_datadir}/kdevappwizard/templates/plasmapotdprovider.tar.bz2
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.keyboardindicator.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma_applet_dict.desktop
%{_datadir}/kservices5/plasma-runner-character.desktop
%{_datadir}/kservices5/plasma-runner-character_config.desktop
%{_datadir}/kservices5/plasma-runner-konsoleprofiles.desktop
%{_datadir}/metainfo/org.kde.plasma.keyboardindicator.appdata.xml
%{_datadir}/metainfo/org.kde.plasma_applet_dict.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.colorpicker/contents/ui/logic.js
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardindicator
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardindicator/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardindicator/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardindicator/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardindicator/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardindicator/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardindicator/contents/ui/configAppearance.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardindicator/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardindicator/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardindicator/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch/contents/ui/layout.js
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/CompactRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/ForecastView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/FullRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/IconAndTextItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/SwitchPanel.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/config/ConfigAppearance.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/config/ConfigUnits.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/config/ConfigWeatherStation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/config/WeatherStationPicker.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather/contents/ui/config/WeatherStationPickerDialog.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma_applet_dict
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma_applet_dict/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma_applet_dict/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma_applet_dict/contents/config/config.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma_applet_dict/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma_applet_dict/contents/ui/ConfigDictionaries.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma_applet_dict/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma_applet_dict/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma_applet_dict/metadata.json

%files devel
%defattr(644,root,root,755)
%{_includedir}/plasma/potdprovider
%{_libdir}/cmake/PlasmaPotdProvider
