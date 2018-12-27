%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		ksudoku
Summary:	ksudoku
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	e514458e74868c28e8a102f57774a6e1
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5OpenGL-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= 4.9.0
BuildRequires:	kf5-extra-cmake-modules >= 5.30.0
BuildRequires:	kf5-karchive-devel >= 5.31.0
BuildRequires:	kf5-kconfig-devel >= 5.31.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.31.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.31.0
BuildRequires:	kf5-kcrash-devel >= 5.31.0
BuildRequires:	kf5-kdoctools-devel >= 5.31.0
BuildRequires:	kf5-kguiaddons-devel >= 5.31.0
BuildRequires:	kf5-ki18n-devel >= 5.31.0
BuildRequires:	kf5-kiconthemes-devel >= 5.31.0
BuildRequires:	kf5-kio-devel >= 5.31.0
BuildRequires:	kf5-kjobwidgets-devel >= 5.31.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.31.0
BuildRequires:	kf5-kxmlgui-devel >= 5.31.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSudoku is a logic-based symbol placement puzzle. The player has to
fill a grid so that each column, row as well as each square block on
the game field contains only one instance of each symbol.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/ksudokurc
%attr(755,root,root) %{_bindir}/ksudoku
%{_desktopdir}/org.kde.ksudoku.desktop
%{_iconsdir}/hicolor/128x128/apps/ksudoku.png
%{_iconsdir}/hicolor/16x16/apps/ksudoku.png
%{_iconsdir}/hicolor/32x32/apps/ksudoku.png
%{_datadir}/ksudoku
%dir %{_datadir}/kxmlgui5/ksudoku
%{_datadir}/kxmlgui5/ksudoku/ksudokuui.rc
%{_datadir}/metainfo/org.kde.ksudoku.appdata.xml
