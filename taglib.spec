
%define 	_ver	0.96
%define		_snap	031204

Summary:	A tag library for reading and editing audio meta data
Summary(pl):	Biblioteka tag do odczytu i edycji metadanych dotycz±cych d¼wiêku
Name:		taglib
Version:	%{_ver}.%{_snap}
Release:	2
License:	GPL
Group:		X11/Libraries
# (temporary?) (pre-)release URL: http://ktown.kde.org/~wheeler/taglib/%{name}-%{version}.tar.gz
# From kdeextragear-2 kde cvs module
Source0:	http://ep09.pld-linux.org/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	b95a5c0a17b0ec058689fb64e0507a0d
URL:		http://ktown.kde.org/~wheeler/taglib/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.1.93.%{_snap}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tag library needed for juk application which is part of
kdemultimedia package.

%description -l pl
Biblioteka tag wykorzystywana przez program juk, bed±cego czê¶ci±
pakietu kdemultimedia.

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
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

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
%{_libdir}/libtag.la

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/taglib-config
%attr(755,root,root) %{_libdir}/libtag.so
%{_includedir}/taglib
