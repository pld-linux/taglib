
%define		_snap	031105

Summary:	A tag library
Summary(pl):	Biblioteka tag
Name:		taglib
Version:	0.95.%{_snap}
Release:	1
License:	GPL
Group:		X11/Libraries
# From kdeextragear-2 kde cvs module
Source0:	http://www.kernel.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	81cb7cdb95ed16b1045772dc05a34623
BuildRequires:	kdelibs-devel >= 9:3.1.93	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tag library needed for juk application which is part of kdemultimedia
package.

%description -l pl
Biblioteka tag wykorzystywana przez program juk, bed±cego czê¶ci± pakietu
kdemultimedia.

%package devel
Summary:	libtag - header files
Summary(pl):	libtag - pliki nag³ówkowe
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
A tag library - header files.

%description devel -l pl
Biblioteka tag - pliki nag³ówkowe.

%prep
%setup -q -n %{name}-%{_snap}

%build

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final

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
%{_libdir}/libtag.la
%attr(755,root,root) %{_libdir}/libtag.so.*.*.*

%files devel
%attr(755,root,root) %{_bindir}/taglib-config
%{_includedir}/taglib
%{_libdir}/libtag.so
