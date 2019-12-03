#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zathura-pdf-poppler
Version  : 0.2.9
Release  : 1
URL      : https://github.com/pwmt/zathura-pdf-poppler/archive/0.2.9/zathura-pdf-poppler-0.2.9.tar.gz
Source0  : https://github.com/pwmt/zathura-pdf-poppler/archive/0.2.9/zathura-pdf-poppler-0.2.9.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Zlib
Requires: zathura-pdf-poppler-data = %{version}-%{release}
Requires: zathura-pdf-poppler-lib = %{version}-%{release}
Requires: zathura-pdf-poppler-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(poppler-glib)
BuildRequires : pkgconfig(zathura)

%description
zathura-pdf-poppler
===================
The zathura-pdf-poppler plugin adds PDF support to zathura by using the poppler
rendering library.

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
%setup -q -n zathura-pdf-poppler-0.2.9
cd %{_builddir}/zathura-pdf-poppler-0.2.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1575401636
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/zathura-pdf-poppler
cp %{_builddir}/zathura-pdf-poppler-0.2.9/LICENSE %{buildroot}/usr/share/package-licenses/zathura-pdf-poppler/d592a09f73efa9efb4b69124a1b9475d6dabc5fd
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.pwmt.zathura-pdf-poppler.desktop
/usr/share/metainfo/org.pwmt.zathura-pdf-poppler.metainfo.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/zathura/libpdf-poppler.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zathura-pdf-poppler/d592a09f73efa9efb4b69124a1b9475d6dabc5fd
