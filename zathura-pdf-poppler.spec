#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v13
# autospec commit: 2659038
#
Name     : zathura-pdf-poppler
Version  : 0.3.2
Release  : 16
URL      : https://github.com/pwmt/zathura-pdf-poppler/archive/0.3.2/zathura-pdf-poppler-0.3.2.tar.gz
Source0  : https://github.com/pwmt/zathura-pdf-poppler/archive/0.3.2/zathura-pdf-poppler-0.3.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Zlib
Requires: zathura-pdf-poppler-data = %{version}-%{release}
Requires: zathura-pdf-poppler-lib = %{version}-%{release}
Requires: zathura-pdf-poppler-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(poppler-glib)
BuildRequires : pkgconfig(zathura)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
zathura-pdf-poppler
===================
zathura is a highly customizable and functional document viewer based on the girara user interface
library and several document libraries. This plugin for zathura provides PDF support using the
`poppler` rendering library.

%package data
Summary: data components for the zathura-pdf-poppler package.
Group: Data

%description data
data components for the zathura-pdf-poppler package.


%package lib
Summary: lib components for the zathura-pdf-poppler package.
Group: Libraries
Requires: zathura-pdf-poppler-data = %{version}-%{release}
Requires: zathura-pdf-poppler-license = %{version}-%{release}

%description lib
lib components for the zathura-pdf-poppler package.


%package license
Summary: license components for the zathura-pdf-poppler package.
Group: Default

%description license
license components for the zathura-pdf-poppler package.


%prep
%setup -q -n zathura-pdf-poppler-0.3.2
cd %{_builddir}/zathura-pdf-poppler-0.3.2
pushd ..
cp -a zathura-pdf-poppler-0.3.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720453567
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/zathura-pdf-poppler
cp %{_builddir}/zathura-pdf-poppler-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/zathura-pdf-poppler/82e4486e3f81dda3b9626879cc039f3f5d1036a8 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.pwmt.zathura-pdf-poppler.desktop
/usr/share/metainfo/org.pwmt.zathura-pdf-poppler.metainfo.xml

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/zathura/libpdf-poppler.so
/usr/lib64/zathura/libpdf-poppler.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zathura-pdf-poppler/82e4486e3f81dda3b9626879cc039f3f5d1036a8
