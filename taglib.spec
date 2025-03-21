Summary:	A tag library for reading and editing audio meta data
Summary(pl.UTF-8):	Biblioteka tag do odczytu i edycji metadanych dotyczących dźwięku
Name:		taglib
Version:	1.13.1
Release:	2
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
#Source0Download: http://taglib.org/
Source0:	https://taglib.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	2fe6089da73ad414aa1b982b83415362
Patch0:		pc.patch
URL:		https://taglib.org/
BuildRequires:	cmake >= 3.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TagLib is a library for reading and editing the meta-data of several
popular audio formats. Currently it supports both ID3v1 and ID3v2 for
MP3 files, Ogg Vorbis comments and ID3 tags and Vorbis comments in
FLAC, MPC, Speex, WavPack TrueAudio, WAV, AIFF, MP4 and ASF files.

%description -l pl.UTF-8
TagLib to biblioteka do odczytu i edycji metadanych kilku popularnych
formatów dźwiękowych. Aktualnie obsługiwane są znaczniki ID3v1 i ID3v2
w plikach MP3, komentarze Ogg Vorbis oraz znaczniki ID3 i komentarze
Vorbis w plikach FLAC, MPC, Speex, WavPack TrueAudio, WAV, AIFF, MP4 i
ASF.

%package devel
Summary:	libtag - header files
Summary(pl.UTF-8):	libtag - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	zlib-devel

%description devel
Header files for tag library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki tag.

%package examples
Summary:	Example codes for taglib
Summary(hu.UTF-8):	Példaprogramok
Summary(pl.UTF-8):	Przykładowe programy w postaci źródłowej dla tagliba
Group:		Development/Libraries
BuildArch:	noarch

%description examples
Example codes for taglib.

%description examples -l hu.UTF-8
Példaprogramok.

%description examples -l pl.UTF-8
Przykładowe programy w postaci źródłowej dla tagliba.

%prep
%setup -q
%patch -P0 -p1

%build
install -d build
cd build
%cmake .. \
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
%doc AUTHORS NEWS
%attr(755,root,root) %{_libdir}/libtag.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtag.so.1
%attr(755,root,root) %{_libdir}/libtag_c.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtag_c.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/taglib-config
%attr(755,root,root) %{_libdir}/libtag.so
%attr(755,root,root) %{_libdir}/libtag_c.so
%{_pkgconfigdir}/taglib.pc
%{_pkgconfigdir}/taglib_c.pc
%{_includedir}/taglib

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
