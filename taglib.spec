Summary:	A tag library for reading and editing audio meta data
Summary(pl):	Biblioteka tag do odczytu i edycji metadanych dotycz±cych d¼wiêku
Name:		taglib
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://ktown.kde.org/~wheeler/taglib/%{name}-%{version}.tar.gz
# Source0-md5:	9595e2cf3e12de96afbe81ae7f4cad33
Patch0:		%{name}-libtool-sanitize.patch
Patch1:		%{name}-am18.patch
URL:		http://ktown.kde.org/~wheeler/taglib/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
# is it needed? taglib links with libstdc++ only
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tag library needed for juk application which is part of
kdemultimedia package.

%description -l pl
Biblioteka tag wykorzystywana przez program juk, bed±cy czê¶ci±
pakietu kdemultimedia.

%package devel
Summary:	libtag - header files
Summary(pl):	libtag - pliki nag³ówkowe
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for tag library.

%description devel -l pl
Pliki nag³ówkowe biblioteki tag.

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
