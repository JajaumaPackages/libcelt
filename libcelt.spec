Name:           libcelt
Version:        0.11.1
Release:        1%{?dist}
Summary:        An audio codec for use in low-delay speech and audio communication

License:        BSD
URL:            http://www.celt-codec.org/
Source0:        http://downloads.xiph.org/releases/celt/celt-%{version}.tar.gz

BuildRequires:  libogg-devel

%description
CELT (Constrained Energy Lapped Transform) is an ultra-low delay audio
codec designed for realtime transmission of high quality speech and audio.
This is meant to close the gap between traditional speech codecs
(such as Speex) and traditional audio codecs (such as Vorbis).


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        -n celt-utils
Summary:        CELT command line decoder and encoder

%description    -n celt-utils
This package provides CELT command line decoder and encoder utilities.


%prep
%setup -q -n celt-%{version}


%build
%configure --disable-static --enable-custom-modes

sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license COPYING
%doc README TODO
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%files -n celt-utils
%{_bindir}/*


%changelog
* Thu Aug 11 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.11.1-1
- Public release
