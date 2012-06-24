
Summary:	A tag library for reading and editing audio meta data
Summary(pl):	Biblioteka tag do odczytu i edycji metadanych dotycz�cych d�wi�ku
Name:		taglib
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://ktown.kde.org/~wheeler/taglib/%{name}-%{version}.tar.gz
# Source0-md5:	9595e2cf3e12de96afbe81ae7f4cad33
URL:		http://ktown.kde.org/~wheeler/taglib/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tag library needed for juk application which is part of
kdemultimedia package.

%description -l pl
Biblioteka tag wykorzystywana przez program juk, bed�cego cz�ci�
pakietu kdemultimedia.

%package devel
Summary:	libtag - header files
Summary(pl):	libtag - pliki nag��wkowe
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
A tag library - header files.

%description devel -l pl
Biblioteka tag - pliki nag��wkowe.

%prep
%setup -q

%build
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
