Summary:	A tag library for reading and editing audio meta data
Summary(pl.UTF-8):	Biblioteka tag do odczytu i edycji metadanych dotyczących dźwięku
Name:		taglib
Version:	1.7
Release:	1
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
Source0:	http://ktown.kde.org/~wheeler/files/src/%{name}-%{version}.tar.gz
# Source0-md5:	6a7e312668f153fa905a81714aebc257
URL:		http://ktown.kde.org/~wheeler/taglib.html
BuildRequires:	cmake >= 2.6.2
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.577
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
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for tag library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki tag.

%package examples
Summary:	Example codes for taglib
Summary(hu.UTF-8):	Példaprogramok
Summary(pl.UTF-8):	Przykładowe programy w postaci źródłowej dla tagliba
Group:		Development/Libraries

%description examples
Example codes for taglib.

%description examples -l hu.UTF-8
Példaprogramok.

%description examples -l pl.UTF-8
Przykładowe programy w postaci źródłowej dla tagliba.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
	-DWITH_ASF=ON \
	-DWITH_MP4=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtag.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtag.so.1
%attr(755,root,root) %{_libdir}/libtag_c.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtag_c.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/taglib-config
%{_libdir}/libtag.so
%{_libdir}/libtag_c.so
%{_pkgconfigdir}/taglib.pc
%{_pkgconfigdir}/taglib_c.pc
%{_includedir}/taglib

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
