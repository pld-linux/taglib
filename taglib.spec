Summary:	A tag library for reading and editing audio meta data
Summary(pl):	Biblioteka tag do odczytu i edycji metadanych dotycz�cych d�wi�ku
Name:		taglib
Version:	1.1
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://developer.kde.org/%7Ewheeler/files/src/%{name}-%{version}.tar.gz
# Source0-md5:	a805368c41d22393cf23ca0f741adc57
Patch0:		%{name}-libtool-sanitize.patch
Patch1:		%{name}-am18.patch
URL:		http://ktown.kde.org/~wheeler/taglib/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tag library needed for juk application which is part of
kdemultimedia package.

%description -l pl
Biblioteka tag wykorzystywana przez program juk, bed�cy cz�ci�
pakietu kdemultimedia.

%package devel
Summary:	libtag - header files
Summary(pl):	libtag - pliki nag��wkowe
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for tag library.

%description devel -l pl
Pliki nag��wkowe biblioteki tag.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.* admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
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
%attr(755,root,root) %{_libdir}/libtag_c.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/taglib-config
%attr(755,root,root) %{_libdir}/libtag.so
%attr(755,root,root) %{_libdir}/libtag_c.so
%{_libdir}/libtag.la
%{_libdir}/libtag_c.la
%{_includedir}/taglib
