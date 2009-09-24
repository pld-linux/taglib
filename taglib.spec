Summary:	A tag library for reading and editing audio meta data
Summary(pl.UTF-8):	Biblioteka tag do odczytu i edycji metadanych dotyczących dźwięku
Name:		taglib
Version:	1.6
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://ktown.kde.org/~wheeler/files/src/%{name}-%{version}.tar.gz
# Source0-md5:	5ecad0816e586a954bd676a86237d054
Patch0:		%{name}-libtool-sanitize.patch
Patch1:		kde-ac260-lt.patch
Patch2:		taglib-am.patch
URL:		http://ktown.kde.org/~wheeler/taglib.html
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tag library needed for juk application which is part of
kdemultimedia package.

%description -l pl.UTF-8
Biblioteka tag wykorzystywana przez program juk, będący częścią
pakietu kdemultimedia.

%package devel
Summary:	libtag - header files
Summary(pl.UTF-8):	libtag - pliki nagłówkowe
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for tag library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki tag.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp -f /usr/share/automake/config.* admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
	--enable-asf \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtag.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtag.so.?
%attr(755,root,root) %{_libdir}/libtag_c.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtag_c.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/taglib-config
%{_libdir}/libtag.so
%{_libdir}/libtag_c.so
%{_libdir}/libtag.la
%{_libdir}/libtag_c.la
%{_pkgconfigdir}/taglib.pc
%{_pkgconfigdir}/taglib_c.pc
%{_includedir}/taglib
