%define		kdeplasmaver	5.4.0
%define		qtver		5.3.2
%define		kpname		kdeplasma-addons

Summary:	All kind of addons to improve your Plasma experience
Name:		kp5-%{kpname}
Version:	5.4.0
Release:	2
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	d9876ebbd99cd3285b86fe6205857eea
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
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdesignerplugin-devel
BuildRequires:	kf5-ki18n-devel
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
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	scim-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
All kind of addons to improve your Plasma experience.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
/etc/xdg/comic.knsrc
%attr(755,root,root) %{_libdir}/kimpanel-ibus-panel
%attr(755,root,root) %{_libdir}/kimpanel-scim-panel
%attr(755,root,root) %ghost %{_libdir}/libplasmacomicprovidercore.so.1
%attr(755,root,root) %{_libdir}/libplasmacomicprovidercore.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_krunner_audioplayercontrol.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_krunner_dictionary.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_krunner_spellcheck.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_comic.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_audioplayercontrol.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_converter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_datetime.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_dictionary.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_spellcheck.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/applets/plasma_applet_comic.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_comic.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_kimpanel.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_konsoleprofiles.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma_comic_krossprovider.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/fifteenpuzzle
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/fifteenpuzzle/libfifteenpuzzleplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/fifteenpuzzle/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/kimpanel
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/kimpanel/libkimpanelplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/kimpanel/qmldir
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
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.kickerdash
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.kimpanel.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.konsoleprofiles.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.notes.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.showdesktop.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.systemloadviewer.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.timer.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.webbrowser.desktop
%{_datadir}/kservices5/plasma-dataengine-comic.desktop
%{_datadir}/kservices5/plasma-dataengine-kimpanel.desktop
%{_datadir}/kservices5/plasma-dataengine-konsoleprofiles.desktop
%{_datadir}/kservices5/plasma-runner-audioplayercontrol.desktop
%{_datadir}/kservices5/plasma-runner-audioplayercontrol_config.desktop
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
%{_datadir}/plasma/desktoptheme/default/widgets/notes.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/timer.svgz
%{_datadir}/plasma/plasmoids/org.kde.plasma.calculator
%{_datadir}/plasma/plasmoids/org.kde.plasma.comic
%{_datadir}/plasma/plasmoids/org.kde.plasma.fifteenpuzzle
%{_datadir}/plasma/plasmoids/org.kde.plasma.fuzzyclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickerdash
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel
%{_datadir}/plasma/plasmoids/org.kde.plasma.konsoleprofiles
%{_datadir}/plasma/plasmoids/org.kde.plasma.notes
%{_datadir}/plasma/plasmoids/org.kde.plasma.showdesktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemloadviewer
%{_datadir}/plasma/plasmoids/org.kde.plasma.timer
%{_datadir}/plasma/plasmoids/org.kde.plasma.webbrowser
%{_datadir}/plasma/services/kimpanel.operations
%{_datadir}/plasma/services/org.kde.plasma.dataengine.konsoleprofiles.operations
%{_datadir}/plasma/wallpapers/org.kde.haenau
%{_datadir}/plasma/wallpapers/org.kde.hunyango
